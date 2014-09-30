from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from dueExcel.views import mytest

# Uncomment the next two lines to enable the admin:
import xadmin
xadmin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'due.views.home', name='home'),
    # url(r'^due/', include('due.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(xadmin.site.urls), name='xadmin'),
    url(r'^test/', mytest),
)

urlpatterns += staticfiles_urlpatterns()