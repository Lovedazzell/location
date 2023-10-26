from django import forms
from django.contrib.auth.forms import AuthenticationForm ,UsernameField



class LoginForm(AuthenticationForm):
    password = forms.CharField(label_suffix='', widget=forms.PasswordInput(attrs={'class':'form-control ','placeholder':'Password','id':'floatingPassword'}))
    username = UsernameField(label_suffix='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username','id':'floatingInput'}))

