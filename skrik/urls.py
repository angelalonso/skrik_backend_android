from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from skrik.views import *

urlpatterns = patterns('',
    url(r'^user/(?P<username>\w{1,50})/$', get_userid_data),
# USEREMAIL SHOULD BE USERACCOUNT
    url(r'^getnewid/(?P<useremail>.{1,100})/$', getnew_userid),
#    url(r'^saveid/(?P<userid>\w{1,50})/name/(?P<username>.{1,50})/email/(?P<useremail>.{1,100})/regid/(?P<regid>.{1,200})/$', save_userdata),
    url(r'^saveid/(?P<userid>\w{1,50})/name/(?P<username>.{1,50})/acc/(?P<useraccount>.{1,100})/regid/(?P<regid>.{1,200})/$', save_user),
    url(r'^searchusers/(?P<word2search>\w{1,50})/$', search_users),
    url(r'^getusers/(?P<userid>\w{1,50})/$', get_rest_of_users),
    url(r'^getusername/(?P<userid>\w{1,50})/$', get_userid_username),
    url(r'^getnews/(?P<userid>\w{1,50})/$', get_news),
    url(r'^gotmsg/(?P<key>\w{1,50})/$', news_confirmed),
    url(r'^newmessage/(?P<message>[\w|\W]+)/userfrom/(?P<userfrom>.{1,20})/userto/(?P<userto>.{1,20})/timestamp/(?P<timestamp>.{1,14})/$', add_message),
    url(r'^poke/(?P<user_from>\w{1,50})/(?P<user_to>\w{1,50})/$', add_poke),
    url(r'^cleanall/(?P<username>\w{1,50})/$', cleanall_pokes),
    (r'^500/$', TemplateView.as_view(template_name="404.html")),
    (r'^404/$', TemplateView.as_view(template_name="404.html")),
    url(r'^$', TemplateView.as_view(template_name="404.html"))
)
