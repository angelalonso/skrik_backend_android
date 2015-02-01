from django.conf.urls import patterns, include, url
from skrik.views import *

urlpatterns = patterns('',
    url(r'^user/(?P<username>\w{1,50})/$', get_userid_data),
    url(r'^getnewid/(?P<useremail>.{1,100})/$', getnew_userid),
    url(r'^saveid/(?P<userid>\w{1,50})/name/(?P<username>.{1,50})/email/(?P<useremail>.{1,100})/regid/(?P<regid>.{1,200})/$', save_userdata),
    url(r'^getusers/(?P<userid>\w{1,50})/$', get_rest_of_users),
    url(r'^getusername/(?P<userid>\w{1,50})/$', get_userid_username),
    url(r'^getnews/(?P<userid>\w{1,50})/$', get_news),
    url(r'^poke/(?P<user_from>\w{1,50})/(?P<user_to>\w{1,50})/$', add_poke),
    url(r'^cleanall/(?P<username>\w{1,50})/$', cleanall_pokes)
)
