from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

from Graduation_Work_With_Django import settings
from .forms import LoginUserForm
from .models import *
from RRIT.views import get_sidebar, get_settings, get_search


def login_user(request):
    if request.method == 'POST':
        form=LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'],
                                password=cd['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form= LoginUserForm()
    return render(request, 'users/login.html', {'form':form})
def logout_user(request):
    logout(request)
    return HttpResponse("logout")

def users_all(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    app_models = get_sidebar()
    function_name, breadcrumb_ru, action_model, action_models_s, eddit_name, array_of_data, count, array_of_th = get_settings(User)
    return render(request, 'RRIT/view_all.html',
                  { 'add': 'add/',
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

def user_id(request, UsersID):
    app_models = get_sidebar()

    function_name, breadcrumb_ru, action_model, action_models_s, eddit_name, array_of_data, count, array_of_th = get_settings(User)
    user = User.objects.get(pk = UsersID)

    breadcrumb_ru += " › " + user.surname + " " + user.name + ' ' + user.lastname + " " + user.email
    return render(request, 'users/user.html',
                  {'user': user,
                    'function_name': function_name,
                   # 'breadcrumbs': breadcrumbs,
                   'breadcrumb_ru': breadcrumb_ru,
                   'app_models': app_models,
                   'action_model': action_model,
                   'eddit_name': eddit_name,
                   'action_models_s': action_models_s,
                   })


def users_search(request):
    arg = request.GET.get('search')
    function_name, breadcrumb_ru, action_model, action_models_s, eddit_name, array_of_data, count, array_of_th = get_search(
        User, arg)
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

def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница users не найдена')
