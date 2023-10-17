from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *
from RRIT.views import get_sidebar, get_settings


def IncidentsALL(request):
    app_models = get_sidebar()
    Incidents_all, function_name, breadcrumb_ru, action_model, action_models_s, eddit_name, array_of_data, count,array_of_th = get_settings(Incidents)
    # breadcrumbs = [Incidents_all.model._meta.app_label]
    return render(request, 'RRIT/view_all.html',
                  {'function_name': function_name,
                   'breadcrumb_ru': breadcrumb_ru,
                   'app_models': app_models,
                   'action_model': action_model,
                   'eddit_name': eddit_name,
                   'action_models_s': action_models_s,
                   'array_of_data': array_of_data,
                   'datas': Incidents_all,
                   'array_of_th': array_of_th,
                   })


def IncidentsID(request, IncidentId):
    print(request.GET)
    return HttpResponse(f"Страница конкретного Incident <p>{IncidentId}</p>")

def Incidents_Search(request, IncidentSearch):
    print(request.GET)
    return HttpResponse(f"Страница поиска Incident <p>{IncidentSearch}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница инцидентов не найдена')
