from django import forms
from django.contrib.auth.models import User
from django.contrib import messages


class User_form(forms.ModelForm):
    password    =forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':' Enter your password'}))
    username    =forms.CharField(widget=forms.TextInput(attrs={'placeholder':' Enter your username'}))
    email    =forms.CharField(widget=forms.EmailInput(attrs={'placeholder':' Enter your Email'}))

    class Meta:
        model   =User
        fields  =['username','password','email']

class Login_form(forms.Form):
    username    =forms.CharField(max_length=50,label='username' ,widget=forms.TextInput(
        attrs={
            'placeholder':' Username/mobile/email '
        }
    ))
    password    =forms.CharField(max_length=50,
                             label='password',
                             widget=forms.PasswordInput(
                               attrs={'placeholder':' Enter password Here'}
                             )

                             )