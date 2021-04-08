from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=255, help_text='eg. youremail@anymail.com')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')
