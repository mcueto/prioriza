from django.shortcuts import render
from django.urls import reverse
from django.views.generic import (
    CreateView,
    ListView,
)
from django.views.generic.base import TemplateView
from polls.models import (
    Poll,
)
from polls.forms import (
    PollForm,
)


class IndexView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'PRIORIZA INDEX VIEW TEMPLATE'

        return context


class PollListView(ListView):
    model = Poll
    context_object_name = 'polls'
    template_name = "poll/list.html"


class PollCreateView(CreateView):
    template_name = 'poll/create.html'
    form_class = PollForm
    model = Poll

    def get_success_url(self, **kwargs):
        """If form is valid, return the user to Poll list view."""
        success_url = reverse(
            'poll_list'
        )

        return success_url

    def get_initial(self, **kwargs):
        """Set initial value of Form fields."""
        initial_data = super(PollCreateView, self).get_initial(
            **kwargs
        )

        initial_data['current_status'] = 'created'

        return initial_data
