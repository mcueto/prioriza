from django.shortcuts import render
from django.views.generic import (
    ListView,
)
from django.views.generic.base import TemplateView
from polls.models import (
    Poll,
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
