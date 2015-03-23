from django.conf.urls import patterns, url, include
from Nexquality import views

urlpatterns = patterns('',
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^profile/$', views.user_profile, name='user_profile'),
    url(r'^profile/project/$', views.UserProjectListView.as_view(), name='project_list'),
    url(r'^profile/project/(?P<pk>\d+)/$', views.ProjectDetailView.as_view(), name='project_detail'),
    url(r'^profile/project/add/$', views.ProjectCreationView.as_view(), name='project_create'),
    url(r'^profile/project/delete/(?P<pk>\d+)/$', views.project_delete, name='project_delete'),
    url(r'^profile/project/update/(?P<pk>\d+)/$', views.project_update, name='project_update'),
    url(r'^registration/subscription/$', views.subscription, name='subscription')
)
