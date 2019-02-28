"""polls app models."""
import uuid
from py3votecore.irv import IRV
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from rest_framework_apicontrol.mixins import (
    TrackableModelMixin,
    UniqueIDModelMixin,
)

# Fields constants
CODE_FIELD_MAX_LENGTH = 128
NAME_FIELD_MAX_LENGTH = 128

# Poll status field choices
POLL_STATUS_CHOICES = (
    ('created', 'created'),
    ('open', 'open'),
    ('finished', 'finished'),
    ('archived', 'archived'),
)


class Poll(TrackableModelMixin, UniqueIDModelMixin):
    code = models.CharField(
        max_length=CODE_FIELD_MAX_LENGTH
    )
    name = models.CharField(
        max_length=NAME_FIELD_MAX_LENGTH
    )
    description = models.TextField(
        blank=True
    )
    budget = models.FloatField(
        default=0
    )
    current_status = models.CharField(
        max_length=CODE_FIELD_MAX_LENGTH,
        choices=POLL_STATUS_CHOICES,
        default='created'
    )

    def get_winners(self):
        winners = []
        budget = self.budget
        vote_list = self.pollvote_set.all()

        for poll_option in self.polloption_set.all():
            ballots = []

            for vote in vote_list:
                ballot = []
                ballot_data = vote.poll_option_selections.exclude(
                    poll_option__unique_id__in=winners
                ).exclude(
                    poll_option__cost__gt=budget
                ).order_by('priority').values_list(
                  'poll_option__unique_id',
                  flat=True
                )

                for data in ballot_data:
                    ballot.append(str(data))

                if len(ballot) > 0:
                    ballots.append({
                        "count": 1,
                        "ballot": ballot
                    })

            if len(ballots) > 0:
                irv = IRV(ballots)
                winners.append(irv.winner)

                poll_option2 = PollOption.objects.get(unique_id=irv.winner)
                budget -= poll_option2.cost

        return PollOption.objects.filter(
            unique_id__in=winners
        )

    def get_loosers(self):
        discarded_poll_options = self.polloption_set.all().difference(
            self.get_winners()
        )

        return discarded_poll_options

    def __str__(self):
        """Return the model instance item name in django admin."""
        return '{name} - {created_at}'.format(
            name=self.name,
            created_at=self.created_at
        )


class PollOption(TrackableModelMixin, UniqueIDModelMixin):
    name = models.CharField(
        max_length=NAME_FIELD_MAX_LENGTH
    )
    description = models.TextField(
        blank=True
    )
    cost = models.FloatField(
        default=0
    )
    poll = models.ForeignKey(
        'poll',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        """Return the model instance item name in django admin."""
        return '{name} - {created_at}'.format(
            name=self.name,
            created_at=self.created_at
        )


class PollOptionSelection(TrackableModelMixin, UniqueIDModelMixin):
    poll_option = models.ForeignKey(
        'polloption',
        on_delete=models.CASCADE,
    )
    priority = models.IntegerField()

    def __str__(self):
        """Return the model instance item name in django admin."""
        return '{name} - {created_at}'.format(
            name=self.poll_option.name,
            created_at=self.created_at
        )


class PollVote(TrackableModelMixin, UniqueIDModelMixin):
    poll = models.ForeignKey(
        'poll',
        on_delete=models.CASCADE,
    )
    poll_option_selections = models.ManyToManyField(
        'polloptionselection'
    )
    voter_user = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
    )

    class Meta:
        unique_together = (("poll", "voter_user"),)

    def __str__(self):
        """Return the model instance item name in django admin."""
        return '{unique_id} - {created_at}'.format(
            unique_id=self.unique_id,
            created_at=self.created_at
        )
