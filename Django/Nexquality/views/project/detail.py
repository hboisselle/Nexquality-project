from Nexquality.views.mixins import LoginRequiredMixin
from Nexquality.models import Project
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


@login_required
def project_detail_view(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    active_users = project.get_active_users()
    inactive_users = project.get_inactive_users()


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Project
    template_name = "project/detail.html"
    pk_url_kwarg = "project_id"
