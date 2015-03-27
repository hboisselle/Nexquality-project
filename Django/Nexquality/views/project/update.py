from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.contrib.auth.decorators import login_required
from Nexquality.models import Project, ProjectUser
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory
from django import forms


@login_required
def update(request, pk):
    if pk is None:
        project = Project()
    else:
        project = get_object_or_404(Project, pk=pk)

    project_users = ProjectUser.get(project.id=pk)

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
        'title': 'Modify project: '+project.name,
        'project_id': pk,
        'form': project_form,
        'users': users,
    })


class ProjectUserForm(forms.ModelForm):
    out_date = forms.DateField(required=False)

    class Meta:
        model = ProjectUser
        fields = ['user', 'role', 'in_date', 'out_date']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'is_done']
