"""polls app models."""
import uuid
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
    title = models.CharField(
        max_length=NAME_FIELD_MAX_LENGTH
    )
    description = models.TextField(
        blank=True
    )
    current_status = models.CharField(
        max_length=CODE_FIELD_MAX_LENGTH,
        choices=POLL_STATUS_CHOICES
    )
    created_at = models.DateTimeField(
        default=timezone.now
    )
    updated_at = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):
        """Return the model instance item name in django admin."""
        return '{title} - {created_at}'.format(
            title=self.title,
            created_at=self.created_at
        )


class PollOption(models.Model):
    unique_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(
        max_length=NAME_FIELD_MAX_LENGTH
    )
    description = models.TextField(
        blank=True
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
        return '{title} - {created_at}'.format(
            title=self.title,
            created_at=self.created_at
        )
