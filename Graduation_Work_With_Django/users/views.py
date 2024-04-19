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
    return redirect('users:login')

def users_all(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    data = get_settings(User)
    data1 = {
        'add': 'add/',
    }

    data = data | data1
    return render(request, 'RRIT/view_all.html',context=data)

def user_id(request, UsersID):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    user = User.objects.get(pk = UsersID)

    password_hash = user.password.split('$')
    solt = password_hash[2][0:6]
    hash = password_hash[3][0:6]

    data = get_settings(User)
    data['breadcrumb_ru'] += " › " + user.surname + " " + user.name + ' ' + user.lastname + " " + user.email
    data1 = {
        'solt': solt,
        'hash': hash,
        'user': user,
    }
    data = data | data1
    return render(request, 'users/user.html',context=data)
def user_delete(request, UsersID):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    user = User.objects.get(pk=UsersID)
    user.delete()
    return redirect('users:Users_all')

def users_search(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    arg = request.GET.get('search')
    data = get_search(User,arg)
    return render(request, 'RRIT/view_all.html',context=data)
def users_positions(request):
    return render(request, 'Position/position.html')




def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница users не найдена')


