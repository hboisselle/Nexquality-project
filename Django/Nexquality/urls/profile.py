from django.conf.urls import patterns, url
from Nexquality.views import profile


urlpatterns = patterns('',
    url(r'^$', profile.profile_list, name='list'),
    url(r'^chart_json_data/$', profile.chart_json_data, name='chart_json_data'),
    url(r'^(?P<username>\w+)/$', profile.profile_detail, name='detail'),

)
