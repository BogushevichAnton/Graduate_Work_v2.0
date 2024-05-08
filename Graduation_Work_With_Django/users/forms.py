from django import forms

from users.models import Positions
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from users.models import User
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = '__all__'

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(
            '<a href="{}">Изменить пароль</a>'
        ),
    )
    class Meta:
        model = User
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        password = self.fields.get("password")
        if password:
            password.help_text = password.help_text.format(
                f"../../{self.instance.pk}/password/"
            )



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