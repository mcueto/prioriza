from rest_framework import (
    viewsets,
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
