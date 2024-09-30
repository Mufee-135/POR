# profiles/urls.py

from django.urls import path
from .views import HomeView, ProfileDetailView, ProjectListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('projects/', ProjectListView.as_view(), name='project_list'),
]

