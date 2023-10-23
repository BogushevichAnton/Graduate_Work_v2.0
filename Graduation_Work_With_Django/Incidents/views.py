from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *
from RRIT.views import get_sidebar, get_settings, get_search


def incidents_all(request):
    if request.GET.get('search'):
        return incidents_search(request)
    else:
        app_models = get_sidebar()
        function_name, breadcrumb_ru, action_model, action_models_s, eddit_name, array_of_data, count, array_of_th = get_settings(Incidents)
        return render(request, 'RRIT/view_all.html',
                      {'function_name': function_name,
                       'breadcrumb_ru': breadcrumb_ru,
                       'app_models': app_models,
                       'action_model': action_model,
                       'eddit_name': eddit_name,
                       'action_models_s': action_models_s,
                       'array_of_data': array_of_data,
                       'array_of_th': array_of_th,
                       'count': count,
                       })


def incidents_id(request, IncidentId):
    print(request.GET)
    return HttpResponse(f"Страница конкретного Incident <p>{IncidentId}</p>")

def incidents_search(request):
    arg = request.GET.get('search')
    function_name, breadcrumb_ru, action_model, action_models_s, eddit_name, array_of_data, count, array_of_th = get_search(
        Incidents, arg)
    app_models = get_sidebar()
    return render(request, 'RRIT/view_all.html',
                  {'function_name': function_name,
                   'breadcrumb_ru': breadcrumb_ru,
                   'app_models': app_models,
                   'action_model': action_model,
                   'eddit_name': eddit_name,
                   'action_models_s': action_models_s,
                   'array_of_data': array_of_data,
                   'array_of_th': array_of_th,
                   'count': count,
                   })

def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница инцидентов не найдена')
