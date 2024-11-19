from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
         widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'class': 'login__input'
        })
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'login__input'
        }))