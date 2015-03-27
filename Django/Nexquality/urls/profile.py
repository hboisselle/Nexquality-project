from django.conf.urls import patterns, url
from Nexquality.views import profile


urlpatterns = patterns('',
    url(r'^profile/$', profile.user_profile, name='user_profile'),
)
