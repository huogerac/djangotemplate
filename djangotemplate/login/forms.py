import floppyforms as forms
from floppyforms.widgets import PasswordInput
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm, forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=PasswordInput())

