from django.shortcuts import render, redirect
from Graduation_Work_With_Django import settings
from RRIT.views import get_settings, get_search, permission_edit_required
from Subdivisions.forms import AddSubdivisionsForm
from Subdivisions.models import Subdivisions
from django.contrib.auth.decorators import login_required
import json
@login_required
@permission_edit_required('Subdivisions.subdivision_all')
def subdivisions_all(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    if request.GET.get('search'):
        return
    else:

        data = get_settings(Subdivisions, 1 )
        data1 = {
            'add': 'add/',
        }
        data = data | data1
        return render(request, 'RRIT/view_all.html',context=data )


@login_required
@permission_edit_required('Subdivisions.subdivision_id')
def subdivision_id(request, Subdivision_ID):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    data = get_settings(Subdivisions)
    subdivision_breadcrumb = Subdivisions.objects.select_related().get(pk = Subdivision_ID)
    subdivisions = Subdivisions.objects.select_related().filter(pk=Subdivision_ID).values('description', 'latitude', 'longitude', 'address','abbreviation')
    data['breadcrumb_ru'] += " › " + subdivision_breadcrumb.abbreviation
    list_data_json = json.dumps(list(subdivisions))
    data1 = {
        'subdivision': subdivision_breadcrumb,
        'data':list_data_json,
    }
    data = data | data1
    return render(request, 'Subdivisions/id.html',context=data)
@login_required
@permission_edit_required('Subdivisions.subdivision_map')
def subdivisions_map(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    data = get_settings(Subdivisions)
    data['breadcrumb_ru'] += " › " +  'Карта подразделений'

    subdivision_breadcrumb = Subdivisions.objects.select_related().values('description', 'latitude', 'longitude', 'address', 'abbreviation')
    list_data_json = json.dumps(list(subdivision_breadcrumb))
    data1 = {
        'data':list_data_json,
    }
    data = data | data1
    return render(request, 'Subdivisions/map.html', context=data)
@login_required
@permission_edit_required('Subdivisions.subdivision_add')
def subdivisions_add(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    if request.method == 'POST':
        form = AddSubdivisionsForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('Subdivision_ID', obj.pk)
    else:
        form = AddSubdivisionsForm()
    data = get_settings(Subdivisions)
    data1 = {
        'form':form,
    }
    data = data | data1
    return render(request, 'Subdivisions/add.html',context=data)
@login_required
@permission_edit_required('Subdivisions.subdivision_change')
def subdivision_change(request, Subdivision_ID):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    subdivision_breadcrumb = Subdivisions.objects.select_related().get(pk = Subdivision_ID)
    if request.method == 'POST':
        form = AddSubdivisionsForm(request.POST, instance=subdivision_breadcrumb)
        if form.is_valid():
            obj = form.save()
            return redirect('Subdivision_ID', obj.pk)
    else:
        form = AddSubdivisionsForm()
        form.fields['address'].widget.attrs['value'] = subdivision_breadcrumb.address
        form.fields['latitude'].widget.attrs['value'] = subdivision_breadcrumb.latitude
        form.fields['longitude'].widget.attrs['value'] = subdivision_breadcrumb.longitude
        form.fields['abbreviation'].widget.attrs['value'] = subdivision_breadcrumb.abbreviation

    subdivisions = Subdivisions.objects.select_related().filter(pk=Subdivision_ID).values('description', 'latitude', 'longitude', 'address','abbreviation')

    list_data_json = json.dumps(list(subdivisions))
    data = get_settings(Subdivisions)
    data['breadcrumb_ru'] += " › " + subdivision_breadcrumb.abbreviation
    data1 = {
        'subdivision':subdivision_breadcrumb,
        'form':form,
        'data': list_data_json
    }
    data = data | data1
    return render(request, 'Subdivisions/change.html',context=data)
@login_required
@permission_edit_required('Subdivisions.subdivision_all')
def subdivisions_search(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    arg = request.GET.get('search')
    data = get_search(Subdivisions, arg, 1)
    data['action_model'] = 'Subdivisions'
    return render(request, 'RRIT/view_all.html',context=data)
@login_required
@permission_edit_required('Subdivisions.subdivision_delete')
def subdivision_delete(request, Subdivision_ID):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    subdivision_breadcrumb = Subdivisions.objects.select_related().get(pk = Subdivision_ID)
    subdivision_breadcrumb.delete()
    return redirect('Subdivisions_all')