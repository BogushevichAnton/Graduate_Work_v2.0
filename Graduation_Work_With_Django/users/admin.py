from django.contrib import admin

from django.contrib import admin
from collections import OrderedDict

from django.contrib import admin
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AdminPasswordChangeForm
from users.models import User, Group
from users.forms import *
# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

class CustomUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    change_user_password_template = 'admin/auth/user/change_password.html'
    fieldsets =(
        (None, {"classes": ("wide",), 'fields': ('email', 'password')}),
        ('Должность', {'fields': ('position',)}),
        ('Подразделение', {'fields': ('subdivision',)}),
        ('Личная информация', {'fields': ('name', 'surname', 'lastname')}),
        ('Группы', {'fields': ('groups',)}),
        ('Права доступа', {'fields': ('user_permissions',)}),
    )

    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2')}),
        ('Личная информация', {'fields': ('name', 'surname', 'lastname')}),
        ('Группы', {'fields': ('groups',)}),
        ('Права доступа', {'fields': ('user_permissions',)}),
    )



    list_filter = ('is_superuser',)
    list_display = ('id', 'name', 'surname', 'lastname',)
    list_display_links = ('id', 'name')
    search_fields = ('email', 'surname', 'lastname')
    ordering = ('email', 'name', 'surname')
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User, CustomUserAdmin)
