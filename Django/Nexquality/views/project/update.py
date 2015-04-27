from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from Nexquality.models import Project, ProjectUser, ProjectUserRole
from django import forms
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


@login_required
def update(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    users = User.objects.all()
    project_user_roles = ProjectUserRole.objects.all()
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project = form.save()
    else:
        form = ProjectForm(instance=project)
    return render(request, "project/update.html", {
        'form': form, 'users': users, 'project_user_roles': project_user_roles
        })


@login_required
def add_user(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        role_id = request.POST.get('project_user_role', False)
        role = ProjectUserRole.objects.get(id=role_id)
        for key, value in request.POST.iteritems():
            string_lookup = 'user_username_'
            if string_lookup in key:
                username = key[len(string_lookup):]
                user = User.objects.get(username=username)
                project_user, created = ProjectUser.objects.get_or_create(
                        user=user, project=project, role=role, out_date=None)
                if created:
                    project_user.save()

    return redirect(reverse('Nexquality:project:update',
                            args=(project.id,)))


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'is_done']


@login_required
def inactivate_user(request, project_id, project_user_id):
    project_user = get_object_or_404(ProjectUser, pk=project_user_id)
    project_user.inactivate()
    project_user.save()
    return redirect(reverse('Nexquality:project:update', args=(project_id,)))
