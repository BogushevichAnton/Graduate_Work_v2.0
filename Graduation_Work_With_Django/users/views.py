from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotFound
from .models import *
def UsersALL(request):
    Users_ALL = User.objects.all()
    function_name = 'views_all'
    breadcrumb_ru = Users_ALL.model._meta.verbose_name_plural
    # breadcrumbs = [Incidents_all.model._meta.app_label]

    return render(request, 'RRIT/view_all.html',
                  {'function_name': function_name,
                   # 'breadcrumbs': breadcrumbs,
                   'breadcrumb_ru': breadcrumb_ru})

def UsersID(request, UsersID):
    print(request.GET)
    return HttpResponse(f"Страница конкретного users <p>{UsersID}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница users не найдена')
