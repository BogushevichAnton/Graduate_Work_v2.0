from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *
from RRIT.views import get_sidebar

def IncidentsALL(request):
    Incidents_all = Incidents.objects.all()
    function_name = 'views_all'
    breadcrumb_ru = Incidents_all.model._meta.verbose_name_plural
    app_models = get_sidebar()
    action_model = Incidents_all.model._meta.app_label
    #breadcrumbs = [Incidents_all.model._meta.app_label]
    return render(request, 'RRIT/view_all.html',
                  {'function_name': function_name,
                   #'breadcrumbs': breadcrumbs,
                   'breadcrumb_ru': breadcrumb_ru,
                   'app_models': app_models,
                   'action_model': action_model,
                   })


def IncidentsID(request, IncidentId):
    print(request.GET)
    return HttpResponse(f"Страница конкретного Incident <p>{IncidentId}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница инцидентов не найдена')
