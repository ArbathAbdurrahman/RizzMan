from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'kotak',
            'placeholder': 'Username or Email',
            'required': True,
        }),
        label="Username or Email"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'kotak-pass',
            'placeholder': 'Password',
            'required': True,
        }),
        label="Password"
    )
