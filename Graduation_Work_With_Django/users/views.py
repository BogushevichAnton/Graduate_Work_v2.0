from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotFound
from .models import *
from RRIT.views import get_sidebar

def UsersALL(request):
    Users_ALL = User.objects.all()
    function_name = 'views_all'
    action_model = Users_ALL.model._meta.app_label
    breadcrumb_ru = Users_ALL.model._meta.verbose_name_plural
    # breadcrumbs = [Incidents_all.model._meta.app_label]
    app_models = get_sidebar()
    return render(request, 'RRIT/view_all.html',
                  {'function_name': function_name,
                   # 'breadcrumbs': breadcrumbs,
                   'breadcrumb_ru': breadcrumb_ru,
                   'app_models': app_models,
                   'action_model': action_model,
                   })

def UsersID(request, UsersID):
    print(request.GET)
    return HttpResponse(f"Страница конкретного users <p>{UsersID}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница users не найдена')
