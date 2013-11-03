from django.contrib.auth import authenticate, get_user_model
import floppyforms as forms
from floppyforms.widgets import PasswordInput
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm, forms.Form):
    """
	Override the default authentication
    """
    message_incorrect_password = "email/username or password invalid."
    message_inactive = "This account is inactive."

    username = forms.CharField(label="email or username", max_length=76)
    password = forms.CharField(widget=PasswordInput())

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if '@' in username:
            UserModel = get_user_model()
            user_email = UserModel._default_manager.filter(email__iexact=username)
            if user_email:
            	username = user_email[0].username

        if username and password:
            self.user_cache = authenticate(username=username, password=password)
            if (self.user_cache is None):
                raise forms.ValidationError(self.message_incorrect_password)
            if not self.user_cache.is_active:
                raise forms.ValidationError(self.message_inactive)
        self.check_for_test_cookie()
        return self.cleaned_data
