from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from Nexquality.models import Project
from django.shortcuts import get_object_or_404


@login_required
def delete(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if project.created_by == request.user:
        project.delete()
        return HttpResponseRedirect(reverse('Nexquality:project:list'))
    else:
        return HttpResponseRedirect(reverse('Nexquality:project:update', args=(project_id,)))
