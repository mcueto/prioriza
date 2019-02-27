from rest_framework import (
    serializers,
)
from .models import (
    Poll,
    PollOption,
    PollOptionSelection,
)


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = (
            '__all__'
        )


class PollOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollOption
        fields = (
            '__all__'
        )


class PollOptionSelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollOptionSelection
        fields = (
            '__all__'
        )
