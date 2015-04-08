from Nexquality.views.mixins import LoginRequiredMixin
from Nexquality.models import Commit
from django.views import generic


class CommitDetailView(LoginRequiredMixin, generic.DetailView):
    model = Commit
    template_name = "project/commit/detail.html"
    pk_url_kwarg = "commit_id"
