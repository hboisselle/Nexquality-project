from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from Nexquality.models import Project
from django.shortcuts import get_object_or_404


@login_required
def delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if project.created_by == request.user:
        project.delete()
        return HttpResponseRedirect(reverse('Nexquality:project:list'))
    else:
        return HttpResponseRedirect(reverse('Nexquality:project:update', args=(pk,)))
