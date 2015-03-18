from django.conf.urls import patterns, url, include
from Nexquality import views

urlpatterns = patterns('',
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^accounts/profile/$', views.user_profile, name='user_profile'),
    url(r'^registration/subscription/$', views.subscription, name='subscription'),
)
