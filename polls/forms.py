"""polls app forms."""
from django.forms import (
    ModelForm,
)
from .models import (
    Poll,
)


class PollForm(ModelForm):
    """Poll model form."""

    class Meta:
        model = Poll
        fields = [
            # 'unique_id',
            'code',
            'title',
            'description',
            'current_status',
            # 'created_at',
            # 'updated_at',
        ]
