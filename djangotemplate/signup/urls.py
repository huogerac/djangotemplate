from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
from django.views.generic import RedirectView

from registration.backends.default.views import RegistrationView
from registration.backends.default.views import ActivationView

from signup.forms import RegistrationSignupForm
from signup.views import UserProfileRegistrationView

urlpatterns = patterns('',

	#1 register
	url(r'^accounts/register/$', RegistrationView.as_view(form_class=RegistrationSignupForm), 
						   name='registration_register'),

	#2 show message about the activation email
	url(r'^accounts/register/complete/$', TemplateView.as_view(template_name='registration/registration_complete.html'),
                           name='registration_complete'),

	#3 active by email link
	url(r'^accounts/activate/(?P<activation_key>\w+)/$', ActivationView.as_view(),
                           name='registration_activate'),

	#4 redirect to user profile
	url(r'^activate/complete/$', RedirectView.as_view(url='/signup/accounts/userprofile/'),
                           name='registration_activation_complete'),

	#5 ask extra fields
	url(r'^accounts/userprofile/$', UserProfileRegistrationView.as_view(), name='finish_userprofile'),

	#6 welcome message
	url(r'^accounts/registration/complete/$', TemplateView.as_view(template_name='signup/registration_complete.html'),
                           name='registration_and_activation_complete'),

)
