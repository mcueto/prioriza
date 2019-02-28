from django.contrib import admin
from .models import (
    Poll,
    PollOption,
    PollOptionSelection,
    PollVote,
)

admin.site.register(Poll)
admin.site.register(PollOption)
admin.site.register(PollOptionSelection)
admin.site.register(PollVote)
