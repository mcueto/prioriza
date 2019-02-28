from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import (
    CreateView,
    ListView,
)
from django.views.generic.base import TemplateView
from rest_framework.renderers import JSONRenderer
from polls.models import (
    Poll,
)
from polls.serializers import (
    PollOptionSerializer,
)


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class UserListView(LoginRequiredMixin, ListView):
    model = get_user_model()
    context_object_name = 'users'
    template_name = "users/list.html"


class UserCreateView(LoginRequiredMixin, CreateView):
    template_name = 'users/create.html'
    form_class = UserCreationForm
    model = get_user_model()

    def get_success_url(self, **kwargs):
        """If form is valid, return the user to Users list view."""
        success_url = reverse(
            'user_list'
        )

        return success_url



class PollListView(LoginRequiredMixin, ListView):
    model = Poll
    context_object_name = 'polls'
    template_name = "poll/list.html"
    ordering = ['-created_at']


class PollCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'poll/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['api_base_url'] = self.request.build_absolute_uri('../api')
        context['poll_list_url'] = reverse(
            'poll_list'
        )
        return context


class PollDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'poll/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        poll = Poll.objects.get(unique_id=kwargs.get('unique_id'))
        poll_options_data = JSONRenderer().render(
            PollOptionSerializer(
                poll.polloption_set.all().order_by('created_at'),
                many=True
            ).data
        ).decode()

        context['api_base_url'] = self.request.build_absolute_uri('../../api')
        context['poll_detail_url'] = reverse(
            'poll_detail',
            kwargs={
                'unique_id': poll.unique_id
            }
        )
        context['poll'] = poll
        context['poll_options_data'] = poll_options_data

        context['votes_cast'] = poll.pollvote_set.count()
        context['users_count'] = get_user_model().objects.all().count()

        context['voted_by_current_user'] = poll.pollvote_set.filter(
            voter_user=self.request.user
        ).exists()

        return context
