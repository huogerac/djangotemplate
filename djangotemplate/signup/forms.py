from django.utils.translation import ugettext_lazy as _
#from django import forms
import floppyforms as forms
from floppyforms.widgets import PasswordInput, HiddenInput, CheckboxInput, EmailInput #TextInput
from django.contrib.auth.models import User

from registration.forms import RegistrationFormTermsOfService

class RegistrationSignupForm(RegistrationFormTermsOfService, forms.Form):

    username = forms.CharField(widget=HiddenInput(), label='', required=False)
    email = forms.EmailField(widget=EmailInput(attrs={'placeholder': 'Enter a valid email'}), label=_("E-mail"))
    password1 = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'Password'}), label=_("Password"))
    password2 = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'Confirm Password'}), label=_("Password (again)"))

    tos = forms.BooleanField(widget=CheckboxInput,
                             label=_(u'I have read and agree to the Terms of Service'),
                             error_messages={'required': _("You must agree to the terms to register")})

    def clean_email(self):
        """
        Validate that the supplied email address is unique for the
        site.
        
        """
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
        return self.cleaned_data['email']

    def clean(self):
        
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields didn't match."))

        if 'email' in self.cleaned_data:
            #TODO: make sure the username is unique
            username = self.cleaned_data['email']
            self.cleaned_data['username'] = username[:username.find('@')]

        return self.cleaned_data