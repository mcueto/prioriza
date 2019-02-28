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


class PollOptionSelectionCreateSerializer(serializers.Serializer):
    poll_option_unique_id = serializers.UUIDField()
    priority = serializers.IntegerField()

    class Meta:
        fields = (
            'poll_option_unique_id',
            'priority',
        )


class PollCreateSerializer(serializers.Serializer):
    poll = PollCreateSerializer()
    poll_options = PollOptionCreateSerializer(many=True)

    class Meta:
        fields = (
            'poll',
            'poll_options',
        )


class PollVoteCreateSerializer(serializers.Serializer):
    poll_unique_id = serializers.UUIDField()
    poll_option_selections = PollOptionSelectionCreateSerializer(many=True)

    class Meta:
        fields = (
            'poll_unique_id',
            'poll_option_selections',
        )
