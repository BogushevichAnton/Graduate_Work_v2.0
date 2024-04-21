from django import forms

from users.models import Positions


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


class PositionForm(forms.ModelForm):
    class Meta:
        model = Positions
        fields = '__all__'
        widgets = {
            'positions': forms.TextInput(attrs={
                                              'placeholder': 'введите наименование должности',
                                              'maxlength': '255',
                                                'class': 'vTextField',
                                              }
                                       ),
        }
        labels = {
        }
        error_messages = {
            'positions': {
                'max_length': "Максимальное количество символов - 255.",
                'required': "Обязательное поле - Должность."
            },
        }