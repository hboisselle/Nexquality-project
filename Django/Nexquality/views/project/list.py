from Nexquality.views.mixins import LoginRequiredMixin
from Nexquality.models import Project
from django.views import generic
from django.db.models import Q


class ProjectListView(generic.list.ListView):
    model = Project


class UserProjectListView(LoginRequiredMixin, ProjectListView):
    context_object_name = 'projects'
    template_name = 'project/list.html'

    def get_queryset(self):
        return Project.objects.filter(
            Q(created_by=self.request.user) |
            Q(users=self.request.user)
        ).distinct()
