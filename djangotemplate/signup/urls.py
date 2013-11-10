from django.conf.urls import patterns, url, include


urlpatterns = patterns('',
	
	#registration
	url(r'^accounts/', include('registration.backends.default.urls')),

)
