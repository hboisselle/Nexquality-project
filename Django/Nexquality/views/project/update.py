from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from Nexquality.models import Project, ProjectUser
from django import forms
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView
from Nexquality.views.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError


@login_required
def update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project = form.save()
    else:
        form = ProjectForm(instance=project)
    return render(request, "project/update.html", {'form': form})


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'is_done']


class ProjectUserForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super(ProjectUserForm, self).clean()
        if ProjectUser.objects.filter(project=cleaned_data['project'], user=cleaned_data['user'], out_date=None):
            raise ValidationError("User is already active in the same project")
            del cleaned_data['user']

        return cleaned_data

    class Meta:
        model = ProjectUser
        fields = ['user', 'project', 'role']


class ProjectUserCreateView(LoginRequiredMixin, CreateView):
    model = ProjectUser
    template_name = 'project/add_user.html'
    form_class = ProjectUserForm

    def get_initial(self):
        project = get_object_or_404(Project, pk=self.kwargs['pk'])
        return {'project': project}

    def get_success_url(self):
        return reverse('Nexquality:project:update', args=(self.kwargs['pk'],))


@login_required
def inactivate_user(request, project_id, project_user_id):
    project_user = get_object_or_404(ProjectUser, pk=project_user_id)
    project_user.inactivate()
    project_user.save()
    return redirect(reverse('Nexquality:project:update', args=(project_id,)))
