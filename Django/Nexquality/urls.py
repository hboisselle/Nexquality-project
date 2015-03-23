from django.conf.urls import patterns, url, include
from Nexquality import views

urlpatterns = patterns('',
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^accounts/profile/$', views.user_profile, name='user_profile'),
    url(r'^accounts/profile/projects$', views.UserProjectListView.as_view(), name='user_project_list'),
    url(r'^accounts/profile/projects/(?P<pk>\d+)/$', views.ProjectDetailView.as_view(), name='user_project_detail'),
    url(r'^accounts/profile/projects/create/$', views.ProjectCreationView.as_view(), name='user_project_create'),
    url(r'^accounts/profile/projects/update/(?P<pk>\d+)$', views.project_update, name='user_project_update'),
    url(r'^registration/subscription/$', views.subscription, name='subscription')
)
