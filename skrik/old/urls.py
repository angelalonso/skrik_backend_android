from django.conf.urls import patterns, include, url
from skrik.views import *

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

 
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sample.views.home', name='home'),
    # url(r'^sample/', include('sample.foo.urls')),
 
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
 
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
 #   url(r'aapp/$',myfunction),
 #   url(r'aapp/test/$',myfunction),
 #   url(r'^(?P<poll_id>\d+)/$', myselect, name='myselect'),
 #   url(r'addone/^(?P<value>\d+)/$', register, name='register'),
 #   url(r'^register/', register, name='register'),
 #   url(r'^poke/', transaction, name='transaction'),
#    url(r'^saveid/(?P<userid>\w{1,50})/name/(?P<username>.+?)/email/(?P<useremail>.+?)/$', save_userdata),
    url(r'^user/(?P<username>\w{1,50})/$', get_userid_data),
    url(r'^getusername/(?P<userid>\w{1,50})/$', get_userid_username),
#    url(r'^getnewid/$', getnew_userid_noemail),
    url(r'^getnewid/(?P<useremail>.{1,100})/$', getnew_userid),
#    url(r'^checkid/(?P<userdata>\w{1,50})/$', check_user_data),
    url(r'^saveid/(?P<userid>\w{1,50})/name/(?P<username>.{1,50})/email/(?P<useremail>.{1,100})/regid/(?P<regid>.{1,200})/$', save_userdata),
    url(r'^getusers/(?P<userid>\w{1,50})/$', get_rest_of_users),
    url(r'^getnews/(?P<userid>\w{1,50})/$', get_news),
    url(r'^poke/(?P<user_from>\w{1,50})/(?P<user_to>\w{1,50})/$', add_poke),
    url(r'^cleanall/(?P<username>\w{1,50})/$', cleanall_pokes)
)
