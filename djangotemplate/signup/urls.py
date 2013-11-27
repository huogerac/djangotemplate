from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView

from registration.backends.default.views import RegistrationView
from registration.backends.default.views import ActivationView

from signup.forms import RegistrationSignupForm

urlpatterns = patterns('',
	

	url(r'^accounts/activate/complete/$', TemplateView.as_view(template_name='registration/activation_complete.html'),
                           name='registration_activation_complete'),
	
	url(r'^accounts/activate/(?P<activation_key>\w+)/$', ActivationView.as_view(),
                           name='registration_activate'),

	url(r'^accounts/register/$', RegistrationView.as_view(form_class=RegistrationSignupForm), 
						   name='registration_register'),

	url(r'^accounts/register/complete/$', TemplateView.as_view(template_name='registration/registration_complete.html'),
                           name='registration_complete'),

	url(r'^register/closed/$', TemplateView.as_view(template_name='registration/registration_closed.html'),
                           name='registration_disallowed'),

)
