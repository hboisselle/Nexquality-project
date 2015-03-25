from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from common_views import ProjectListView, LoginRequiredMixin
from Nexquality.models import Project, ProjectUser
from django.contrib.auth.models import User
from django.views.generic import edit
from django.core.urlresolvers import reverse
from django.forms.models import inlineformset_factory
from django import forms
from django.http import HttpResponseRedirect
from django.utils.functional import curry


@login_required
def project_update(request, pk):
    if pk is None:
        project = Project()
    else:
        project = Project.objects.get(id=pk)

    ProjectUserFormset = inlineformset_factory(Project, ProjectUser,
        form=ProjectUserForm,
        extra=1,
        max_num=User.objects.count(),
        fk_name='project',
        can_delete=False,
    )

    ProjectUserFormset.form = staticmethod(curry(ProjectUserForm, project=project))
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

    return render(request, "Nexquality/project_form.html", {
        'title': 'Modify project: '+project.name,
        'form': project_form,
        'project_user_formset': project_user_formset,
    })


@login_required
def project_delete(request, pk):
    project = Project.objects.get(id=pk)
    if project.created_by == request.user:
        project.delete()
        return HttpResponseRedirect(reverse('Nexquality:project_list'))
    else:
        return HttpResponseRedirect(reverse('Nexquality:project_update', args=(pk,)))


class ProjectUserForm(forms.ModelForm):
    user = forms.ModelChoiceField()
    out_date = forms.DateField(required=False)

    def __init__(self, *args, **kwargs):
        project = kwargs.pop('project', None)
        super(ProjectUserForm, self).__init__(*args, **kwargs)

        if project:
            self.fields['user'].queryset = User.objects.exclude(project=project)

    class Meta:
        model = ProjectUser
        fields = ['user', 'role', 'in_date', 'out_date']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'is_done']


class ProjectCreationView(LoginRequiredMixin, edit.CreateView):
    model = Project
    fields = ['name']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(ProjectCreationView, self).form_valid(form)

    def get_success_url(self):
        return reverse('Nexquality:project_update', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(ProjectCreationView, self).get_context_data(**kwargs)
        context['title'] = 'New project'
        return context


class UserProjectListView(LoginRequiredMixin, ProjectListView):
    context_object_name = 'project_list'

    def get_queryset(self):
        return Project.objects.filter(
            users=self.request.user,
            created_by=self.request.user
        )
