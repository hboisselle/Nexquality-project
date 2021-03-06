from django.conf.urls import patterns, url
from Nexquality.views import project


urlpatterns = patterns('',
    url(r'^$', project.UserProjectListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', project.ProjectDetailView.as_view(), name='detail'),
    url(r'^add/$', project.ProjectCreationView.as_view(), name='create'),
    url(r'^delete/(?P<pk>\d+)/$', project.delete, name='delete'),
    url(r'^update/(?P<pk>\d+)/$', project.update, name='update'),
    url(r'^update/(?P<pk>\d+)/add-user$', project.ProjectUserCreateView.as_view(), name='add_user'),
    url(r'^update/(?P<project_id>\d+)/inactivate-user/(?P<project_user_id>\d+)$', project.inactivate_user, name='inactivate_user'),
)
