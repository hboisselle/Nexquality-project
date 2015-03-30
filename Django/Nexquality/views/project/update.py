from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.contrib.auth.decorators import login_required
from Nexquality.models import Project, ProjectUser
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory
from django import forms
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView
from Nexquality.views.mixins import LoginRequiredMixin


@login_required
def update(request, pk):
    if pk is None:
        project = Project()
    else:
        project = get_object_or_404(Project, pk=pk)

    if request.method == 'POST':
        project_form = ProjectForm(
            request.POST,
            instance=project
        )
        if project_form.is_valid():
            project = project_form.save()

    else:
        project_form = ProjectForm(instance=project)

    return render(request, "project/update.html", {
        'form': project_form,
    })


class ProjectUserForm(forms.ModelForm):

    class Meta:
        model = ProjectUser
        fields = ['user', 'role']


class ProjectUserCreateView(LoginRequiredMixin, CreateView):
    model = ProjectUser
    template_name = 'project/add_user.html'

    def form_valid(self, form):
        return super(ProjectUserCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('Nexquality:project:update', args=(self.kwargs['pk'],))


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'is_done']
