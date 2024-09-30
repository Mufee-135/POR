
from django.views.generic import DetailView, ListView, TemplateView
from .models import UserProfile, Project, Portfolio


# profiles/views.py


# Home View
class HomeView(TemplateView):
    template_name = 'profiles/home.html'

# Profile Detail View
class ProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'profiles/profile_detail.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['portfolios'] = self.object.portfolios.all()
        context['projects'] = self.object.projects.all()
        return context

# Project List View
class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.all()
