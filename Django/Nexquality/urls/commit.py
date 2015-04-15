from Nexquality.views.project import commit
from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', commit.ProjectCommitListView.as_view(), name='list'),
    url(r'^(?P<commit_id>\d+)/$', commit.detail, name='detail'),
)
