from django.conf.urls import patterns, url, include
from Nexquality import views

urlpatterns = patterns('',
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^accounts/profile/$', views.user_profile, name='user_profile'),
    url(r'^accounts/profile/projects$', views.UserProjectListView.as_view(), name='user_projects'),
    url(r'^registration/subscription/$', views.subscription, name='subscription')
)
