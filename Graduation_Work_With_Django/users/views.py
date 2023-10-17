from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotFound
from .models import *
from RRIT.views import get_sidebar, get_settings

def UsersALL(request):
    app_models = get_sidebar()
    Users_all, function_name, breadcrumb_ru, action_model, action_models_s, eddit_name, array_of_data, count, array_of_th = get_settings(User)
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

def UsersID(request, UsersID):
    print(request.GET)
    return HttpResponse(f"Страница конкретного users <p>{UsersID}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница users не найдена')
