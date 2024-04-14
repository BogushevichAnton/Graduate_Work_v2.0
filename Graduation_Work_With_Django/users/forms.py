from django import forms

class LoginUserForm(forms.Form):
    email = forms.CharField(label="Email", widget=forms.TextInput(attrs={
    'autocapitalize':'none',
    'autofocus':'autofocus',
    'maxlength':'10',
    'required': 'required',
    'id':'id_username',
    'maxlength':'255',
    }))

    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
    'id':"id_password",
        'autocomplete':"current-password",
    }))