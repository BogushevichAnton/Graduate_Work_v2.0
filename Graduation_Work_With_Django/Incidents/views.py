import json
import locale

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from Graduation_Work_With_Django import settings
from .forms import AddIncidentsForm, AddSpecificationsForm, StatusForm
from .models import *
from RRIT.views import get_settings, get_search, permission_edit_required

@login_required
@permission_edit_required('Incidents.Incidents.incidents_all')
def incidents_all(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    if request.GET.get('search'):
        return incidents_search(request)
    else:
        data = get_settings(request, Incidents, 1)
        return render(request, 'RRIT/view_all.html',context=data)

@login_required
@permission_edit_required('Incidents.Incidents.incidents_id')
def incidents_id(request, IncidentId):
    data = get_settings(request,Incidents)
    try:
        incident_breadcrumb = Incidents.objects.select_related().get(pk = IncidentId)
    except Incidents.DoesNotExist:
        raise Http404("No MyModel matches the given query.")
    incidents = Incidents.objects.filter(pk=IncidentId).select_related().values('description', 'latitude', 'longitude', 'address', 'specification__pattern', 'specification__color', 'time_create', 'user_create__surname', 'user_create__name','user_create__lastname')
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

@login_required
@permission_edit_required('Incidents.Incidents.incidents_all')
def incidents_search(request):
    arg = request.GET.get('search')
    data = get_search(request, Incidents, arg, 1)
    return render(request, 'RRIT/view_all.html', context=data)


@login_required
@permission_edit_required('Incidents.Incidents.incidents_map')
def incidents_map(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    data = get_settings(request,Incidents)
    incidents = Incidents.objects.select_related().values('description', 'latitude', 'longitude','address', 'specification__pattern', 'specification__color', 'time_create', 'user_create__surname', 'user_create__name','user_create__lastname')
    key1 = list(incidents)
    for res in key1:
        res['time_create'] = res['time_create'].strftime('%d %b. %Y  %H:%M')
    list_data_json = json.dumps(key1)
    data1 = {
        'data': list_data_json,
    }
    data = data | data1
    return render(request, 'Incidents/map.html', context=data)


@login_required
@permission_edit_required('Incidents.Incidents.incidents_add')
def incidents_add(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    if request.method == 'POST':
        form = AddIncidentsForm(request.POST)
        form.instance.user_create = request.user
        if form.is_valid():
            obj = form.save()
            obj.time_create = datetime.datetime.now()
            obj.save()
            return redirect('Incidents_ID', obj.pk)
    else:

        form = AddIncidentsForm()
    data = get_settings(request,Incidents)
    data1 = {
        'form': form,
    }
    data = data | data1
    return render(request, 'Incidents/add.html',  context=data)
@login_required
@permission_edit_required('Incidents.Incidents.incidents_change')
def incidents_change(request, IncidentId):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    incident_breadcrumb = Incidents.objects.select_related().get(pk=IncidentId)
    time_start = incident_breadcrumb.time_start
    status = incident_breadcrumb.status
    taken_measures = incident_breadcrumb.taken_measures
    event_check = incident_breadcrumb.status.status
    if request.method == 'POST':
        form = AddIncidentsForm(request.POST, instance=incident_breadcrumb)
        if form.is_valid():
            obj = form.save()
            if request.POST.get('taken_measures', '') != '' and event_check == 'Обнаружено':
                obj.time_start = datetime.datetime.now()
                obj.status = Status.objects.select_related().get(status='В работе')
                obj.save()
            else:
                obj.time_start = time_start
                obj.status = status
                obj.taken_measures = taken_measures
            if request.POST.get('complete', '') != '':
                obj.time_end = datetime.datetime.now()
                obj.status = Status.objects.select_related().get(status='Завершено')
                obj.save()

            obj.save()
            return redirect('Incidents_ID', obj.pk)
    else:
        form = AddIncidentsForm()
        form.fields['address'].widget.attrs['value'] = incident_breadcrumb.address
        form.fields['latitude'].widget.attrs['value'] = incident_breadcrumb.latitude
        form.fields['longitude'].widget.attrs['value'] = incident_breadcrumb.longitude
        form.fields['specification'].initial = incident_breadcrumb.specification.pk
    incident = Incidents.objects.select_related().filter(pk=IncidentId).values('address', 'description', 'latitude', 'longitude',
                                                              'specification__pattern', 'specification__color',
                                                              'time_create', 'user_create__surname', 'user_create__name',
                                                              'user_create__lastname')
    key1 = list(incident)
    key1[0]['time_create'] = key1[0]['time_create'].strftime('%d %b. %Y  %H:%M')
    list_data_json = json.dumps(key1)
    status_help = status.status
    data = get_settings(request,Incidents)
    data['breadcrumb_ru'] += " › " + incident_breadcrumb.description
    data1 = {
        'data': list_data_json,
        'form': form,
        'incident': incident_breadcrumb,
        'status_help':status_help,
    }
    data = data | data1
    return render(request, 'Incidents/change.html', context=data)
@login_required
@permission_edit_required('Incidents.Incidents.incidents_delete')
def incidents_delete(request, IncidentId):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    incident_breadcrumb = Incidents.objects.select_related().get(pk=IncidentId)
    incident_breadcrumb.delete()
    return redirect('Incidents_all')

def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница инцидентов не найдена')
@login_required
@permission_edit_required('Incidents.Incidents.specification_all')
def incidents_specification(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    data = get_settings(request,Specifications, 1)
    data['action_models_s'] = 'Specification'
    data['action_model'] = 'Specifications'
    data1 = {
        'start_model': 'Incidents',
        'add': 'add/'
    }
    data = data | data1
    return render(request, 'RRIT/view_all.html',context=data)
@login_required
@permission_edit_required('Incidents.Incidents.specification_add')
def incidents_specification_add(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    if request.method == 'POST':
        form = AddSpecificationsForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('Specification_ID', obj.pk)
    else:
        data = get_settings(request,Specifications)
        form = AddSpecificationsForm()
    data['action_model'] = 'Specifications'
    data1 = {
            'form': form,
        }
    data = data | data1

    return render(request, 'Specifications/add_specification.html', context=data )
@login_required
@permission_edit_required('Incidents.Incidents.specification_id')
def incidents_specification_id(request, SpecificationsId):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    specification = Specifications.objects.select_related().get(pk=SpecificationsId)

    data = get_settings(request,Specifications)
    data['action_model'] = 'Specifications'
    data1 = {
        'specification':specification,
    }
    data = data | data1

    return render(request, 'Specifications/id_specification.html', context=data)
@login_required
@permission_edit_required('Incidents.Incidents.specification_change')
def incidents_specification_change(request, SpecificationsId):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    specification = Specifications.objects.select_related().get(pk=SpecificationsId)
    if request.method == 'POST':
        form = AddSpecificationsForm(request.POST, instance=specification)
        if form.is_valid():
            obj = form.save()
            return redirect('Specification_ID', obj.pk)
    else:

        form = AddSpecificationsForm()
        form.fields['pattern'].widget.attrs['value'] = specification.pattern
        form.fields['color'].widget.attrs['value'] = specification.color

    data = get_settings(request,Specifications)
    data['action_model'] = 'Specifications'
    data1 = {
        'form': form,
        'specification': specification,
    }
    data = data | data1
    return render(request, 'Incidents.Specifications/change_specification.html', context=data)
@login_required
@permission_edit_required('Incidents.Incidents.specification_delete')
def incidents_specification_delete(request, SpecificationsId):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    specification = Specifications.objects.get(pk=SpecificationsId)
    specification.delete()
    return redirect('Incidents_specification')
@login_required
@permission_edit_required('Incidents.Incidents.specification_all')
def incidents_specification_search(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    arg = request.GET.get('search')
    data = get_search(request, Specifications, arg, 1)
    data['action_model'] = 'Specifications'
    return render(request, 'RRIT/view_all.html',context=data)

@login_required
@permission_edit_required('Incidents.Incidents.status_all')
def incidents_status(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    data = get_settings(request,Status, 1)
    data['action_models_s'] = 'Status'
    data['action_model'] = 'Status'
    data1 = {
        'start_model': 'Incidents',
        'add': 'add/'
    }
    data = data | data1
    return render(request, 'RRIT/view_all.html',context=data)
@login_required
@permission_edit_required('Incidents.Incidents.status_add')
def incidents_status_add(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('StatusID', obj.pk)
    else:
        data = get_settings(request,Specifications)
        form = StatusForm()
    data['action_model'] = 'Status'
    data1 = {
            'form': form,
        }
    data = data | data1

    return render(request, 'Status/add_status.html', context=data )

@login_required
@permission_edit_required('Incidents.Incidents.status_id')
def incidents_status_id(request, StatusID):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    status = Status.objects.select_related().get(pk=StatusID)

    data = get_settings(request,Status)
    data['action_model'] = 'Status'
    data1 = {
        'start_model':'Incidents',
        'status':status,
    }
    data = data | data1

    return render(request, 'Status/id_status.html', context=data)
@login_required
@permission_edit_required('Incidents.Incidents.status_change')
def incidents_status_change(request, StatusID):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    status = Status.objects.select_related().get(pk=StatusID)
    if request.method == 'POST':
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            obj = form.save()
            return redirect('StatusID', obj.pk)
    else:

        form = StatusForm()
        form.fields['status'].widget.attrs['value'] = status.status
        form.fields['description'].widget.attrs['value'] = status.description

    data = get_settings(request,Status)
    data['action_model'] = 'Status'
    data1 = {
        'form': form,
        'status': status,
    }
    data = data | data1
    return render(request, 'Status/change_status.html', context=data)
@login_required
@permission_edit_required('Incidents.Incidents.status_delete')
def incidents_status_delete(request, StatusID):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    status = Status.objects.get(pk=StatusID)
    status.delete()
    return redirect('Incidents_status')
@login_required
@permission_edit_required('Incidents.Incidents.status_all')
def incidents_status_search(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    arg = request.GET.get('search')
    data = get_search(request, Status, arg, 1)
    data['action_model'] = 'Status'
    return render(request, 'RRIT/view_all.html',context=data)



