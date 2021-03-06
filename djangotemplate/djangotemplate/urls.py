from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'templateroger.views.home', name='home'),
    # url(r'^templateroger/', include('templateroger.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^core/', include('core.urls')),
    url(r'^login/', include('login.urls')),
    url(r'^signup/', include('signup.urls')),
)
