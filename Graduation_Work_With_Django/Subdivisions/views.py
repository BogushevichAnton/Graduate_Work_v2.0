from django.shortcuts import render, redirect
from Graduation_Work_With_Django import settings
from RRIT.views import get_sidebar, get_settings, get_search
from Subdivisions.models import Subdivisions


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