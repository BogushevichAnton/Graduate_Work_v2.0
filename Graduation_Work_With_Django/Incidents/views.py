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
        data = get_settings(Incidents)
        return render(request, 'RRIT/view_all.html',context=data)


def incidents_id(request, IncidentId):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    data = get_settings(Incidents)
    incident_breadcrumb = Incidents.objects.get(pk = IncidentId)
    incidents = Incidents.objects.filter(pk=IncidentId).values('description', 'latitude', 'longitude', 'address', 'specification__pattern', 'specification__color', 'time_create', 'user_create__surname', 'user_create__name','user_create__lastname')
    data['breadcrumb_ru'] += " › " + incident_breadcrumb.description
    key1 = list(incidents)
    for res in key1:
        res['time_create'] = res['time_create'].strftime('%d %b. %Y  %H:%M')
    list_data_json = json.dumps(key1)
    if not incident_breadcrumb.taken_measures:
        incident_breadcrumb.taken_measures = 'Еще нет решения'
    data1 = {
        'incident':incident_breadcrumb,
        'data': list_data_json,
    }
    data = data | data1
    return render(request, 'Incidents/index.html', context=data)


def incidents_search(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    arg = request.GET.get('search')
    data = get_search(Incidents, arg)

    return render(request, 'RRIT/view_all.html', context=data)



def incidents_map(request):
    locale.setlocale(locale.LC_ALL, '')
    key = request.user.get_user_permissions()
    key1 = request.user.get_all_permissions()
    key2 = request.user.get_group_permissions()
    key3 = request.user.get_group_permissions
    key4 = request.user.has_perm('Incidents.add_incidents')
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    data = get_settings(Incidents)
    incidents = Incidents.objects.values('description', 'latitude', 'longitude','address', 'specification__pattern', 'specification__color', 'time_create', 'user_create__surname', 'user_create__name','user_create__lastname')
    key1 = list(incidents)
    for res in key1:
        res['time_create'] = res['time_create'].strftime('%d %b. %Y  %H:%M')
    list_data_json = json.dumps(key1)
    data1 = {
        'data': list_data_json,
    }
    data = data | data1
    return render(request, 'Incidents/map.html', context=data)



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
    data = get_settings(Incidents)
    data1 = {
        'form': form,
    }
    data = data | data1
    return render(request, 'Incidents/add.html',  context=data)

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
    incident = Incidents.objects.filter(pk=IncidentId).values('address', 'description', 'latitude', 'longitude',
                                                              'specification__pattern', 'specification__color',
                                                              'time_create', 'user_create__surname', 'user_create__name',
                                                              'user_create__lastname')
    key1 = list(incident)
    key1[0]['time_create'] = key1[0]['time_create'].strftime('%d %b. %Y  %H:%M')
    list_data_json = json.dumps(key1)

    data = get_settings(Incidents)
    data['breadcrumb_ru'] += " › " + incident_breadcrumb.description
    data1 = {
        'data': list_data_json,
        'form': form,
        'incident': incident_breadcrumb,
    }
    data = data | data1
    return render(request, 'Incidents/change.html', context=data)

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
    data = get_settings(Specifications)
    data['action_models_s'] = 'Specification'
    data['action_model'] = 'Specifications'
    data1 = {
        'start_model': 'Incidents',
        'add': 'add/'
    }
    data = data | data1
    return render(request, 'RRIT/view_all.html',context=data)

def incidents_specification_add(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    if request.method == 'POST':
        form = AddSpecificationsForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('Specification_ID', obj.pk)
    else:
        data = get_settings(Specifications)
        form = AddSpecificationsForm()
    data['action_model'] = 'Specifications'
    data1 = {
            'form': form,
        }
    data = data | data1

    return render(request, 'Incidents/add_specification.html', context=data )

def incidents_specification_id(request, SpecificationsId):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    specification = Specifications.objects.get(pk=SpecificationsId)
    form = AddSpecificationsForm()

    data = get_settings(Specifications)
    data['action_model'] = 'Specifications'
    data1 = {
        'form': form,
        'specification':specification,
    }
    data = data | data1

    return render(request, 'Incidents/id_specification.html', context=data)
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

        form = AddSpecificationsForm()
        form.fields['pattern'].widget.attrs['value'] = specification.pattern
        form.fields['color'].widget.attrs['value'] = specification.color

    data = get_settings(Specifications)
    data['action_model'] = 'Specifications'
    data1 = {
        'form': form,
        'specification': specification,
    }
    data = data | data1
    return render(request, 'Incidents/change_specification.html', context=data)
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
    data = get_search(Specifications, arg)
    data['action_model'] = 'Specifications'
    return render(request, 'RRIT/view_all.html',context=data)


