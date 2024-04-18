from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import context

from Graduation_Work_With_Django import settings
from Incidents.models import *
from users.models import *
from django.contrib import admin
from django.apps import apps

all_models = []
def get_sidebar():
    list = apps.get_models()
    app_models = []
    for model in list:
        if model._meta.app_label == 'Incidents':
            app_models.append({
                'name': model._meta.verbose_name_plural,
                'app_label': model._meta.object_name,
                'url_view': '/' + model._meta.app_label + '/' + model._meta.object_name[:-1] + '/',
                'add_url': '/' + model._meta.app_label + '/' + model._meta.object_name[:-1] + '/' + 'add/',
                'change_url': '/' + model._meta.app_label + '/' + model._meta.object_name[:-1] + '/' + 'change/',
            }
            )
        if model._meta.app_label == 'users':
            app_models.append({
                'name': model._meta.verbose_name_plural,
                'app_label': model._meta.app_label,
                'url_view': '/' + model._meta.app_label + '/' + model._meta.app_label[:-1] + '/',
                'add_url': '/' + model._meta.app_label + '/' + model._meta.app_label[:-1] + '/' + 'add/',
                'change_url': '/' + model._meta.app_label + '/' + model._meta.app_label[:-1] + '/' + 'change/',
            }
            )
        if model._meta.app_label == 'Subdivisions':
            app_models.append({
                'name': model._meta.verbose_name_plural,
                'app_label': model._meta.object_name,
                'url_view': '/' + model._meta.app_label + '/' + model._meta.object_name[:-1] + '/',
                'add_url': '/' + model._meta.app_label + '/' + model._meta.object_name[:-1] + '/' + 'add/',
                'change_url': '/' + model._meta.app_label + '/' + model._meta.object_name[:-1] + '/' + 'change/',
            })
    return app_models

def get_settings(model):
    if model._meta.object_name == 'Incidents':
        Model_all = model.objects.all().order_by('-time_create')
    else:
        Model_all = model.objects.all()
    function_name = 'views_all'
    action_model = Model_all.model._meta.app_label
    action_models_s = Model_all.model._meta.app_label[:-1]
    eddit_name = Model_all.model._meta.verbose_name
    breadcrumb_ru = Model_all.model._meta.verbose_name_plural
    array_of_th = []
    array_of_data = []
    for i in range(len(Model_all.model.list_display)):
        array_of_th.append(Model_all.model._meta.get_field(Model_all.model.list_display[i]).verbose_name)

    for data in Model_all:
        help_array = []
        for list in data.list_display:
            help_array.append({
                list: getattr(data, list),
            })

        array_of_data.append({
            data.id: help_array,
        })
    if model._meta.object_name == 'Incidents':
        key = 1
    count = len(array_of_data)
    return function_name, breadcrumb_ru, action_model, action_models_s, eddit_name, array_of_data, count, array_of_th

def get_search(model, arg):
    if model._meta.object_name == 'User':
        filter_model = model.objects.filter(
            Q(email__icontains=arg) | Q(name__icontains=arg) | Q(surname__icontains=arg) | Q(lastname__icontains=arg))
    elif model._meta.object_name == 'Incidents':
        filter_model = model.objects.filter(
            Q(address__icontains=arg) | Q(description__icontains=arg) |Q(user_create__name=arg,user_create__surname=arg, user_create__lastname=arg, _connector=Q.OR) | Q(user_create__fullname__icontains=arg))
    elif model._meta.object_name == 'Specifications':
        filter_model = model.objects.filter(
            Q(pattern__icontains=arg) | Q(color__icontains=arg))
    Model_all = model.objects.all()
    function_name = 'views_all'
    action_model = Model_all.model._meta.app_label
    action_models_s = Model_all.model._meta.app_label[:-1]
    eddit_name = Model_all.model._meta.verbose_name
    breadcrumb_ru = Model_all.model._meta.verbose_name_plural
    array_of_th = []
    array_of_data = []

    for i in range(len(Model_all.model.list_display)):
        array_of_th.append(Model_all.model._meta.get_field(Model_all.model.list_display[i]).verbose_name)

    for mod in filter_model:
        help_array = []
        for list in mod.list_display:
            help_array.append({
                list: getattr(mod, list),
            })
        array_of_data.append({
            mod.id: help_array,
        })

    count = len(array_of_data)
    return function_name, breadcrumb_ru, action_model, action_models_s, eddit_name, array_of_data, count, array_of_th
def index(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    app_models = get_sidebar()
    # app_list = apps.get_models()
    return render(request, 'RRIT/index.html',
                  {'app_models': app_models,})
