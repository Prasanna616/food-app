from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User #RegisterForm is belong to User model
        fields = ['username','email','password1','password2'] #required fields in form
        


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        # Check if user exists in database
        if username and not User.objects.filter(username=username).exists():
            raise forms.ValidationError('User does not exist')
        return username
