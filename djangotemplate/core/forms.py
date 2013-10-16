import floppyforms as forms

class ProfileForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    url = forms.URLField()