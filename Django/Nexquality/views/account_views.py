from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from common_views import ProjectListView, LoginRequiredMixin
from Nexquality.models import Project


@login_required
def user_profile(request):
    return render(request, "accounts/profile.html")


class UserProjectListView(LoginRequiredMixin, ProjectListView):
    context_object_name = 'project_list'
