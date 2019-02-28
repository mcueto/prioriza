"""polls app models."""
import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

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


class Poll(models.Model):
    unique_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
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
    created_at = models.DateTimeField(
        default=timezone.now
    )
    updated_at = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):
        """Return the model instance item name in django admin."""
        return '{name} - {created_at}'.format(
            name=self.name,
            created_at=self.created_at
        )


class PollOption(models.Model):
    unique_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(
        max_length=NAME_FIELD_MAX_LENGTH
    )
    description = models.TextField(
        blank=True
    )
    cost = models.FloatField(
        default=0
    )
    created_at = models.DateTimeField(
        default=timezone.now
    )
    updated_at = models.DateTimeField(
        default=timezone.now
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


class PollOptionSelection(models.Model):
    unique_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    created_at = models.DateTimeField(
        default=timezone.now
    )
    updated_at = models.DateTimeField(
        default=timezone.now
    )
    poll_option = models.ForeignKey(
        'polloption',
        on_delete=models.CASCADE,
    )
    selection_priority = models.IntegerField()

    def __str__(self):
        """Return the model instance item name in django admin."""
        return '{title} - {created_at}'.format(
            title=self.title,
            created_at=self.created_at
        )


class PollVote(models.Model):
    unique_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    created_at = models.DateTimeField(
        default=timezone.now
    )
    updated_at = models.DateTimeField(
        default=timezone.now
    )
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

    unique_together = (("poll", "voter_user"),)

    def __str__(self):
        """Return the model instance item name in django admin."""
        return '{unique_id} - {created_at}'.format(
            unique_id=self.unique_id,
            created_at=self.created_at
        )
