from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from Nexquality.models import Commit


@login_required
def profile_detail(request, username):
    found_user = get_object_or_404(User, username=username)
    commits = Commit.objects.filter(user=found_user)
    
    return render(request, "profile/detail.html", {'found_user': found_user, 'commits': commits})
