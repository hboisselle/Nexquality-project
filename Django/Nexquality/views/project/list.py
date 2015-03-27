from Nexquality.views.mixins import LoginRequiredMixin
from Nexquality.models import Project
from django.views import generic


class ProjectListView(generic.list.ListView):
    model = Project


class UserProjectListView(LoginRequiredMixin, ProjectListView):
    context_object_name = 'project_list'
    template_name = 'project/list.html'

    def get_queryset(self):
        return Project.objects.filter(
            users=self.request.user,
            created_by=self.request.user
        )
