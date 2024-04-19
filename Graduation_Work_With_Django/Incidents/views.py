import json
import locale

from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

from Graduation_Work_With_Django import settings
from .forms import AddIncidentsForm, AddSpecificationsForm
from .models import *
from RRIT.views import get_sidebar, get_settings, get_search, permission_edit_required


@permission_edit_required('Incidents.view_incidents')
def incidents_all(request):
    #key1 = permission_required(request.user)
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    if request.GET.get('search'):
        return incidents_search(request)
    else:
        app_models = get_sidebar()
        function_name, breadcrumb_ru, action_model, action_models_s, eddit_name, array_of_data, count, array_of_th = get_settings(Incidents)
        return render(request, 'RRIT/view_all.html',
                      {'add': 'add/',
                        'function_name': function_name,
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
    incidents = Incidents.objects.filter(pk=IncidentId).values('description', 'latitude', 'longitude', 'address', 'specification__pattern', 'specification__color', 'time_create', 'user_create__surname', 'user_create__name','user_create__lastname')
    breadcrumb_ru += " › " + incident_breadcrumb.description
    key1 = list(incidents)
    for res in key1:
        res['time_create'] = res['time_create'].strftime('%d %b. %Y  %H:%M')
    list_data_json = json.dumps(key1)
    if not incident_breadcrumb.taken_measures:
        incident_breadcrumb.taken_measures = 'Еще нет решения'
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
    locale.setlocale(locale.LC_ALL, '')
    key = request.user.get_user_permissions()
    key1 = request.user.get_all_permissions()
    key2 = request.user.get_group_permissions()
    key3 = request.user.get_group_permissions
    key4 = request.user.has_perm('Incidents.add_incidents')
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    app_models = get_sidebar()
    function_name, breadcrumb_ru, action_model, action_models_s, eddit_name, array_of_data, count, array_of_th = get_settings(
        Incidents)
    incidents = Incidents.objects.values('description', 'latitude', 'longitude','address', 'specification__pattern', 'specification__color', 'time_create', 'user_create__surname', 'user_create__name','user_create__lastname')
    key1 = list(incidents)
    for res in key1:
        res['time_create'] = res['time_create'].strftime('%d %b. %Y  %H:%M')
    list_data_json = json.dumps(key1)

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
        form = AddIncidentsForm(request.POST)
        form.instance.user_create = request.user
        if form.is_valid():
            obj = form.save()
            return redirect('Incidents_ID', obj.pk)
    else:

        form = AddIncidentsForm()
    app_models = get_sidebar()
    function_name, breadcrumb_ru, action_model, action_models_s, eddit_name, array_of_data, count, array_of_th = get_settings(
        Incidents)
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
        form = AddIncidentsForm(request.POST, instance=incident_breadcrumb)
        if form.is_valid():

            obj = form.save()
            return redirect('Incidents_ID', obj.pk)
    else:
        form = AddIncidentsForm()
        form.fields['address'].widget.attrs['value'] = incident_breadcrumb.address
        form.fields['latitude'].widget.attrs['value'] = incident_breadcrumb.latitude
        form.fields['longitude'].widget.attrs['value'] = incident_breadcrumb.longitude
        form.fields['specification'].initial = incident_breadcrumb.specification.pk
    app_models = get_sidebar()
    function_name, breadcrumb_ru, action_model, action_models_s, eddit_name, array_of_data, count, array_of_th = get_settings(
        Incidents)
    incident = Incidents.objects.filter(pk=IncidentId).values('address', 'description', 'latitude', 'longitude',
                                                              'specification__pattern', 'specification__color',
                                                              'time_create', 'user_create__surname', 'user_create__name',
                                                              'user_create__lastname')
    breadcrumb_ru += " › " + incident_breadcrumb.description

    key1 = list(incident)
    key1[0]['time_create'] = key1[0]['time_create'].strftime('%d %b. %Y  %H:%M')

    list_data_json = json.dumps(key1)
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
    start_model = "Incidents"
    return render(request, 'RRIT/view_all.html',
                  {
                      'start_model': start_model,
                      'add': 'add/',
                      'function_name': function_name,
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
def incidents_specification_add(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    if request.method == 'POST':
        form = AddSpecificationsForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('Specification_ID', obj.pk)
    else:
        app_models = get_sidebar()
        function_name, breadcrumb_ru, action_model, action_models_s, eddit_name, array_of_data, count, array_of_th = get_settings(
            Specifications)
        form = AddSpecificationsForm()
    action_model = 'Specifications'
    return render(request, 'Incidents/add_specification.html', {'form': form,
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

def incidents_specification_id(request, SpecificationsId):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    specification = Specifications.objects.get(pk=SpecificationsId)
    app_models = get_sidebar()
    function_name, breadcrumb_ru, action_model, action_models_s, eddit_name, array_of_data, count, array_of_th = get_settings(
        Specifications)
    form = AddSpecificationsForm()
    action_model = 'Specifications'
    return render(request, 'Incidents/id_specification.html', { 'specification': specification,
                                                  'function_name': function_name,
                                                  'breadcrumb_ru': breadcrumb_ru,
                                                  'app_models': app_models,
                                                  'action_model': action_model,
                                                  'eddit_name': eddit_name,
                                                  'action_models_s': action_models_s,
                                                  'array_of_data': array_of_data,
                                                  'array_of_th': array_of_th,
                                                  'count': count,
                                                  })
def incidents_specification_change(request, SpecificationsId):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    specification = Specifications.objects.get(pk=SpecificationsId)
    if request.method == 'POST':
        form = AddSpecificationsForm(request.POST, instance=specification)
        if form.is_valid():
            obj = form.save()
            return redirect('Specification_ID', obj.pk)
    else:
        app_models = get_sidebar()
        function_name, breadcrumb_ru, action_model, action_models_s, eddit_name, array_of_data, count, array_of_th = get_settings(
            Incidents)
        form = AddSpecificationsForm()
        form.fields['pattern'].widget.attrs['value'] = specification.pattern
        form.fields['color'].widget.attrs['value'] = specification.color
    action_model = 'Specifications'
    return render(request, 'Incidents/change_specification.html', {'form': form,
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
def incidents_specification_delete(request, SpecificationsId):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    specification = Specifications.objects.get(pk=SpecificationsId)
    specification.delete()
    return redirect('Incidents_specification')

def incidents_specification_search(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    arg = request.GET.get('search')
    function_name, breadcrumb_ru, action_model, action_models_s, eddit_name, array_of_data, count, array_of_th = get_search(
        Specifications, arg)
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


