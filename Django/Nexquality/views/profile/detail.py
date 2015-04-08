from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


@login_required
def profile_detail(request, username):
    found_user = get_object_or_404(User, username=username)
    return render(request, "profile/detail.html", {'found_user': found_user})
