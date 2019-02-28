"""prioriza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from polls.viewsets import (
    PollViewSet,
    CreatePollAPIView,
    VoteAPIView,
)
from .views import (
    IndexView,
    UserListView,
    UserCreateView,
    PollListView,
    PollCreateView,
    PollDetailView,
    PollResultView,
)


router = DefaultRouter()
router.register(r'polls', PollViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', IndexView.as_view(), name='index'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/create', UserCreateView.as_view(), name='user_create'),
    path('polls/', PollListView.as_view(), name='poll_list'),
    path('polls/create', PollCreateView.as_view(), name='poll_create'),
    path('polls/<uuid:unique_id>/detail', PollDetailView.as_view(), name='poll_detail'),
    path('polls/<uuid:unique_id>/results', PollResultView.as_view(), name='poll_result'),
    path('api/', include(router.urls)),
    path('api/polls_create/', CreatePollAPIView.as_view()),
    path('api/polls_vote/', VoteAPIView.as_view()),
]
