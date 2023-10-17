from django.http import HttpResponse
from django.shortcuts import render
from django.template import context

from Incidents.models import *
from users.models import *
from django.contrib import admin
from django.apps import apps

all_models = []

def get_sidebar():
    list = apps.get_models()
    app_models = []
    for model in list:
        if model._meta.app_label == 'users' or model._meta.app_label == 'Incidents':
            app_models.append({
                'name': model._meta.verbose_name_plural,
                'app_label': model._meta.app_label,
                'url_view': '/' + model._meta.app_label + '/' + model._meta.app_label[:-1] + '/',
                'add_url': '/' + model._meta.app_label + '/' + model._meta.app_label[:-1] + '/' + 'add/',
                'change_url': '/' + model._meta.app_label + '/' + model._meta.app_label[:-1] + '/' + 'change/',
            }
            )
    return app_models

def get_settings(model):
    Model_all = model.objects.all()
    function_name = 'views_all'
    action_model = Model_all.model._meta.app_label
    action_models_s = Model_all.model._meta.app_label[:-1]
    eddit_name = Model_all.model._meta.verbose_name
    breadcrumb_ru = Model_all.model._meta.verbose_name_plural
    array_of_th = []
    array_of_data = []
    for data in Model_all:
        for list in data.list_display:
            if data._meta.get_field(list).verbose_name not in array_of_th:
                array_of_th.append(data._meta.get_field(list).verbose_name)
    for data in Model_all:
        help_array = []
        for list in data.list_display:
            help_array.append({
                list: getattr(data, list),
            })
        array_of_data.append({
            data.id: help_array,
        })
    count = len(array_of_data)
    return Model_all, function_name, breadcrumb_ru, action_model, action_models_s, eddit_name, array_of_data, count, array_of_th


def index(request):
    app_models = get_sidebar()
    # app_list = apps.get_models()
    return render(request, 'RRIT/index.html',
                  {'app_models': app_models,})
