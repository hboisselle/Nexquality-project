from Nexquality.views.mixins import LoginRequiredMixin
from Nexquality.models import Commit, Project
from django.views.generic.list import ListView


class CommitListView(ListView):
    model = Commit


class ProjectCommitListView(LoginRequiredMixin, CommitListView):
    context_object_name = "commits"
    template_name = "project/commit/list.html"

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return Commit.objects.filter(project__id=project_id)

    def get_context_data(self, **kwargs):
        project_id = self.kwargs['project_id']
        context = super(ProjectCommitListView, self).get_context_data(**kwargs)
        context['project'] = Project.objects.get(pk=project_id)
        return context
