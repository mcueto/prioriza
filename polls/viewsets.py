from rest_framework import (
    viewsets,
    authentication,
    permissions,
    status,
)
from rest_framework.views import (
    APIView,
)
from rest_framework.response import (
    Response,
)
from .models import (
    Poll,
    PollOption,
    PollOptionSelection,
    PollVote,
)
from .serializers import (
    PollSerializer,
    PollOptionSerializer,
    PollOptionSelectionSerializer,
    PollCreateSerializer,
    PollVoteCreateSerializer,
)


class PollViewSet(viewsets.ModelViewSet):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()


class PollOptionViewSet(viewsets.ModelViewSet):
    serializer_class = PollOptionSerializer
    queryset = PollOption.objects.all()


class PollOptionSelectionViewSet(viewsets.ModelViewSet):
    serializer_class = PollOptionSelectionSerializer
    queryset = PollOptionSelection.objects.all()


class CreatePollAPIView(APIView):

    def post(self, request, format=None):
        """Create a Poll and it's PollOption related instances."""
        # Serialize request data
        poll_create_serializer = PollCreateSerializer(
            data=request.data
        )

        try:
            if poll_create_serializer.is_valid(raise_exception=True):
                poll_data = poll_create_serializer.validated_data.get('poll')
                poll_options_data = poll_create_serializer.validated_data.get('poll_options')

                poll = Poll.objects.create(
                    **poll_data
                )

                for poll_option_data in poll_options_data:
                    poll_option_data['poll'] = poll
                    poll_option = PollOption.objects.create(
                        **poll_option_data
                    )

            return Response(
                status=status.HTTP_201_CREATED
            )

        except Exception as e:
            return Response(
                status=status.HTTP_400_BAD_REQUEST
            )


class VoteAPIView(APIView):

    def post(self, request, format=None):
        # Serialize request data
        poll_vote_create_serializer = PollVoteCreateSerializer(
            data=request.data
        )

        try:
            if poll_vote_create_serializer.is_valid(raise_exception=True):
                poll_option_selection_list = []

                # Get validated data from serializer
                poll_unique_id = poll_vote_create_serializer.validated_data.get('poll_unique_id')
                poll_option_selections = poll_vote_create_serializer.validated_data.get('poll_option_selections')

                poll = Poll.objects.get(unique_id=poll_unique_id)

                for poll_option_selections_data in poll_option_selections:
                    poll_option = PollOption.objects.get(
                        unique_id=poll_option_selections_data.get('poll_option_unique_id')
                    )
                    priority = poll_option_selections_data.get('priority')

                    poll_option_selection_data = {
                        'poll_option': poll_option,
                        'priority': priority
                    }

                    poll_option_selection = PollOptionSelection.objects.create(
                        **poll_option_selection_data
                    )
                    poll_option_selection_list.append(poll_option_selection)

                poll_vote_data = {
                    'poll': poll,
                    'voter_user': request.user,
                }

                poll_vote = PollVote.objects.create(
                    **poll_vote_data
                )
                poll_vote.poll_option_selections.add(
                    *poll_option_selection_list
                )

            return Response(
                status=status.HTTP_201_CREATED
            )

        except Exception as e:
            return Response(
                status=status.HTTP_400_BAD_REQUEST
            )
