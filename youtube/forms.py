from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=20)
    password = forms.CharField(label='Your password', max_length=20)

class RegisterForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=20)
    password = forms.CharField(label='Your password', max_length=20)
    email = forms.CharField(label='Your name', max_length=20)
    first_name = forms.CharField(label='Your name', max_length=20)
    last_name = forms.CharField(label='Your name', max_length=20)
   
    