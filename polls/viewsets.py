from rest_framework import (
    viewsets,
)
from .models import (
    Poll,
)
from .serializers import (
    PollSerializer,
)


class PollViewSet(viewsets.ModelViewSet):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()
