from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User #RegisterForm is belong to User model
        fields = ['username','email','password1','password2'] #required fields in form
        