from Nexquality.views.mixins import LoginRequiredMixin
from Nexquality.models import Project
from django.views import generic


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Project
