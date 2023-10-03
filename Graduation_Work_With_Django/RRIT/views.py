from django.http import HttpResponse
from django.shortcuts import render
from django.template import context

from Incidents.models import *
from users.models import *
from django.contrib import admin
from django.apps import apps

all_models = []


def index(request):
    list = apps.get_models()
    app_models = []
    for model in list:
        if model._meta.app_label == 'users' or model._meta.app_label == 'Incidents':
            app_models.append({
                'name': model._meta.verbose_name_plural,
                'test': '123',
            }
    )
    app_list = apps.get_models()
    return render(request, 'RRIT/index.html',
                  {'app_models': app_models, 'app_list': app_list, 'title': 'Отслеживание происшествий ОАО "РЖД"'})
