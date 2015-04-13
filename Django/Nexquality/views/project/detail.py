from Nexquality.models import Project
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render


@login_required
def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    context = {}
    context['project'] = project
    context['active_users'] = project.get_active_users()
    latest_commit = project.get_latest_commit()
    if latest_commit:
        context['inactive_users'] = project.get_inactive_users()
        context['metrics'] = latest_commit.metric_set.all()
        context['issues'] = latest_commit.issues.all()
    return render(request, "project/detail.html", context)
