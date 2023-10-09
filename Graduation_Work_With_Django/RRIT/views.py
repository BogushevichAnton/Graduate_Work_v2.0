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

def index(request):
    app_models = get_sidebar()
    # app_list = apps.get_models()
    return render(request, 'RRIT/index.html',
                  {'app_models': app_models,})
