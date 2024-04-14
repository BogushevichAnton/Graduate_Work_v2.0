import json

from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render, redirect

from Graduation_Work_With_Django import settings
from .forms import AddPostForm
from .models import *
from RRIT.views import get_sidebar, get_settings, get_search
from django.core.serializers import serialize

def incidents_all(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
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
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    app_models = get_sidebar()
    function_name, breadcrumb_ru, action_model, action_models_s, eddit_name, array_of_data, count, array_of_th = get_settings(
        Incidents)
    incident_breadcrumb = Incidents.objects.get(pk = IncidentId)
    incident = Incidents.objects.filter(pk=IncidentId).values('address', 'description', 'latitude', 'longitude', 'specification__pattern', 'specification__color')
    breadcrumb_ru += " › " + incident_breadcrumb.description
    list_data_json = json.dumps(list(incident))
    return render(request, 'Incidents/index.html', {'incident': incident_breadcrumb,
                                                    'data': list_data_json ,
                                                    'breadcrumb_ru': breadcrumb_ru,
                                                    'function_name': function_name,
                                                    'app_models': app_models,
                                                    'action_model': action_model,
                                                    'eddit_name': eddit_name,
                                                    'action_models_s': action_models_s,
                                                    'array_of_data': array_of_data,
                                                    'count': count,
                                                    'array_of_th': array_of_th,
                                                    })


def incidents_search(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
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



def incidents_map(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    app_models = get_sidebar()
    function_name, breadcrumb_ru, action_model, action_models_s, eddit_name, array_of_data, count, array_of_th = get_settings(
        Incidents)
    incidents = Incidents.objects.values('description', 'latitude', 'longitude', 'specification__pattern', 'specification__color')
    list_data_json = json.dumps(list(incidents))

    return render(request, 'Incidents/map.html', {'data': list_data_json,
                                                    'breadcrumb_ru': breadcrumb_ru,
                                                    'function_name': function_name,
                                                    'app_models': app_models,
                                                    'action_model': action_model,
                                                    'eddit_name': eddit_name,
                                                    'action_models_s': action_models_s,
                                                    'array_of_data': array_of_data,
                                                    'count': count,
                                                    'array_of_th': array_of_th,
                                                    })



def incidents_add(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('Incidents_ID', obj.pk)
    else:
        app_models = get_sidebar()
        function_name, breadcrumb_ru, action_model, action_models_s, eddit_name, array_of_data, count, array_of_th = get_settings(
            Incidents)
        form = AddPostForm()
    return render(request, 'Incidents/add.html',  {'form': form,
                                                   'function_name': function_name,
                                                   'breadcrumb_ru': breadcrumb_ru,
                                                   'app_models': app_models,
                                                   'action_model': action_model,
                                                   'eddit_name': eddit_name,
                                                   'action_models_s': action_models_s,
                                                   'array_of_data': array_of_data,
                                                   'array_of_th': array_of_th,
                                                   'count': count,
     }
                  )

def incidents_change(request, IncidentId):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    incident_breadcrumb = Incidents.objects.get(pk=IncidentId)
    if request.method == 'POST':
        form = AddPostForm(request.POST, instance=incident_breadcrumb)
        if form.is_valid():
            obj = form.save()
            return redirect('Incidents_ID', obj.pk)
    else:
        app_models = get_sidebar()
        function_name, breadcrumb_ru, action_model, action_models_s, eddit_name, array_of_data, count, array_of_th = get_settings(
            Incidents)
        incident = Incidents.objects.filter(pk=IncidentId).values('address', 'description', 'latitude', 'longitude', 'specification__pattern', 'specification__color')
        breadcrumb_ru += " › " + incident_breadcrumb.description
        list_data_json = json.dumps(list(incident))
        form = AddPostForm()
        form.fields['address'].widget.attrs['value'] = incident_breadcrumb.address
        form.fields['latitude'].widget.attrs['value'] = incident_breadcrumb.latitude
        form.fields['longitude'].widget.attrs['value'] = incident_breadcrumb.longitude
        form.fields['specification'].initial = incident_breadcrumb.specification.pk
    return render(request, 'Incidents/change.html', {
                                                    'form':form,
                                                    'incident': incident_breadcrumb,
                                                    'data': list_data_json ,
                                                    'breadcrumb_ru': breadcrumb_ru,
                                                    'function_name': function_name,
                                                    'app_models': app_models,
                                                    'action_model': action_model,
                                                    'eddit_name': eddit_name,
                                                    'action_models_s': action_models_s,
                                                    'array_of_data': array_of_data,
                                                    'count': count,
                                                    'array_of_th': array_of_th,
                                                    })

def incidents_delete(request, IncidentId):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    incident_breadcrumb = Incidents.objects.get(pk=IncidentId)
    incident_breadcrumb.delete()
    return redirect('Incidents_all')

def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница инцидентов не найдена')

def incidents_specification(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    app_models = get_sidebar()
    function_name, breadcrumb_ru, action_model, action_models_s, eddit_name, array_of_data, count, array_of_th = get_settings(Specifications)
    action_models_s = 'Specification'
    action_model = 'Specifications'
    return render(request, 'RRIT/view_all.html',
                  {'function_name': function_name,
                   # 'breadcrumbs': breadcrumbs,
                   'breadcrumb_ru': breadcrumb_ru,
                   'app_models': app_models,
                   'action_model': action_model,
                   'eddit_name': eddit_name,
                   'action_models_s': action_models_s,
                   'array_of_data': array_of_data,
                   'count': count,
                   'array_of_th': array_of_th,
                   })


