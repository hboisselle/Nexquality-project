from django.shortcuts import get_object_or_404, render
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

    ProjectUserFormset = inlineformset_factory(Project, ProjectUser,
        form=ProjectUserForm,
        extra=0,
        max_num=User.objects.count(),
        fk_name='project',
        can_delete=False,
    )

    if request.method == 'POST':
        project_form = ProjectForm(
            request.POST,
            instance=project
        )
        project_user_formset = ProjectUserFormset(
            request.POST,
            instance=project,
            prefix='project_user'
        )
        if project_form.is_valid() and project_user_formset.is_valid():
            project = project_form.save(commit=False)
            project_user_formset.save()
            project.save()

    else:
        project_form = ProjectForm(instance=project)
        project_user_formset = ProjectUserFormset(
            instance=project,
            prefix='project_user'
        )

    return render(request, "project/update.html", {
        'title': 'Modify project: '+project.name,
        'project_id': pk,
        'form': project_form,
        'project_user_formset': project_user_formset,
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
