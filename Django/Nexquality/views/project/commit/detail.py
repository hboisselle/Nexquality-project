from Nexquality.models import Commit
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def detail(request, project_id, commit_id):
    context = {}
    context['message'] = "Rate this commit"
    commit = Commit.objects.get(pk=commit_id)
    if request.method == "POST":
        score = request.POST['score']
        if score:
            commit.code_review_score = score
            commit.save()
            context['message'] = "Rating saved!"

    context['commit'] = commit
    return render(request, "project/commit/detail.html", context)
