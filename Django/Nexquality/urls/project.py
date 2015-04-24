from django.conf.urls import patterns, url, include
from Nexquality.views import project


urlpatterns = patterns('',
    url(r'^$', project.UserProjectListView.as_view(), name='list'),
    url(r'^(?P<project_id>\d+)/$', project.detail, name='detail'),
    url(r'^add/$', project.ProjectCreationView.as_view(), name='create'),
    url(r'^delete/(?P<project_id>\d+)/$', project.delete, name='delete'),
    url(r'^update/(?P<project_id>\d+)/$', project.update, name='update'),
    url(r'^update/(?P<project_id>\d+)/add-user$', project.add_user, name='add_user'),
    url(r'^update/(?P<project_id>\d+)/inactivate-user/(?P<project_user_id>\d+)$', project.inactivate_user, name='inactivate_user'),
    url(r'^(?P<project_id>\d+)/commit/', include('Nexquality.urls.commit', namespace='commit')),
)
