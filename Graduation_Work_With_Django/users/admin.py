from django.contrib import admin

from django.contrib import admin
from collections import OrderedDict

from django.contrib import admin
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from users.models import User, Group

# Register your models here.

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

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
    password = ReadOnlyPasswordHashField()
    class Meta:
        model = User
        fields = ('email', 'password',)

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class CustomUserAdmin(admin.ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm,
    fieldsets = [
        (
            None,
            {
                "fields": ["email", "password"],
            },
        ),
        (
            'Р›РёС‡РЅС‹Рµ РґР°РЅРЅС‹Рµ',
            {
                "fields": ["name", "surname", "lastname"],
            },
        ),
        (
            'РџСЂР°РІР° РґРѕСЃС‚СѓРїР°',
            {
                "fields": ['groups',],
            },
        ),
    ]
    list_display = ('id', 'name', 'surname', 'lastname', )
    list_display_links = ('id', 'name')
    search_fields = ('email', 'surname', 'lastname')
    ordering = ('email','name', 'surname')
    filter_horizontal = ('groups', 'user_permissions',)
    #list_editable = []

admin.site.register(User, CustomUserAdmin)


