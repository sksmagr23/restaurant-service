from django import forms
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def save(self, request):
        user = super().save(request)
        return user