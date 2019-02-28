from rest_framework import (
    serializers,
)
from .models import (
    Poll,
    PollOption,
    PollOptionSelection,
    PollVote,
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


class PollVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollVote
        fields = (
            '__all__'
        )


# Poll create endpoint serializers
class PollCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = (
            'code',
            'name',
            'description',
            'budget',
        )


class PollOptionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollOption
        fields = (
            'name',
            'description',
        )


class PollCreateSerializer(serializers.Serializer):
    poll = PollCreateSerializer()
    poll_options = PollOptionCreateSerializer(many=True)

    class Meta:
        fields = (
            'poll',
            'poll_options',
        )
