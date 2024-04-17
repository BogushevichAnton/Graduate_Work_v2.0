from django.shortcuts import render, redirect
from Graduation_Work_With_Django import settings
from RRIT.views import get_sidebar, get_settings, get_search
from Subdivisions.forms import AddSubdivisionsForm
from Subdivisions.models import Subdivisions
import json

def subdivisions_all(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    if request.GET.get('search'):
        return
    else:
        app_models = get_sidebar()
        function_name, breadcrumb_ru, action_model, action_models_s, eddit_name, array_of_data, count, array_of_th = get_settings(Subdivisions)
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



def subdivision_id(request, Subdivision_ID):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    app_models = get_sidebar()
    function_name, breadcrumb_ru, action_model, action_models_s, eddit_name, array_of_data, count, array_of_th = get_settings(
        Subdivisions)
    subdivision_breadcrumb = Subdivisions.objects.get(pk = Subdivision_ID)
    subdivisions = Subdivisions.objects.filter(pk=Subdivision_ID).values('description', 'latitude', 'longitude', 'address','abbreviation')

    breadcrumb_ru += " › " + subdivision_breadcrumb.description
    list_data_json = json.dumps(list(subdivisions))
    return render(request, 'Subdivisions/id.html', {'subdivision': subdivision_breadcrumb,
                                                                'data': list_data_json,
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

def subdivisions_map(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    app_models = get_sidebar()
    function_name, breadcrumb_ru, action_model, action_models_s, eddit_name, array_of_data, count, array_of_th = get_settings(
        Subdivisions)
    subdivision_breadcrumb = Subdivisions.objects.values('description', 'latitude', 'longitude', 'address', 'abbreviation')
    list_data_json = json.dumps(list(subdivision_breadcrumb))
    breadcrumb_ru += ' › Карта подразделений'
    return render(request, 'Subdivisions/map.html', {
                                                                'data': list_data_json,
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
    app_models = get_sidebar()
    function_name, breadcrumb_ru, action_model, action_models_s, eddit_name, array_of_data, count, array_of_th = get_settings(
        Subdivisions)
    return render(request, 'Subdivisions/add.html',  {'form': form,
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
