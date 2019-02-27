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
)
from .serializers import (
    PollSerializer,
    PollOptionSerializer,
    PollOptionSelectionSerializer,
    PollCreateSerializer,
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
