from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from common_views import ProjectListView, LoginRequiredMixin
from Nexquality.models import Project, ProjectTeam
from django.views.generic import edit
from django.core.urlresolvers import reverse


@login_required
def user_profile(request):
    return render(request, "accounts/profile.html")


class UserProjectListView(LoginRequiredMixin, ProjectListView):
    context_object_name = 'project_list'

    def get_queryset(self):
        return Project.objects.filter(users=self.request.user)


class ProjectCreationView(LoginRequiredMixin, edit.CreateView):
    model = Project
    fields = ['name']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(ProjectCreationView, self).form_valid(form)

    def get_success_url(self):
        return reverse('Nexquality:user_project_update', args=(self.object.id,))


class ProjectUpdateView(LoginRequiredMixin, edit.UpdateView):
    model = ProjectTeam
