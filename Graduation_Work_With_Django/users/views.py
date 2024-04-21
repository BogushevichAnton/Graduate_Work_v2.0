from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseNotFound, HttpResponseRedirect

from Graduation_Work_With_Django import settings
from .forms import LoginUserForm, PositionForm
from .models import *
from RRIT.views import get_settings, get_search, permission_edit_required


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

@login_required
def logout_user(request):
    logout(request)
    return redirect('users:login')
@login_required
@permission_edit_required('users.user_all')
def users_all(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    data = get_settings(User,1)
    data1 = {
        'add': 'add/',
    }

    data = data | data1
    return render(request, 'RRIT/view_all.html',context=data)
@login_required
@permission_edit_required('users.user_id')
def user_id(request, UsersID):
    user = User.objects.get(pk=UsersID)
    password_hash = user.password.split('$')
    solt = password_hash[2][0:6]
    hash = password_hash[3][0:6]

    data = get_settings(User)
    data['breadcrumb_ru'] += " › " + user.surname + " " + user.name + ' ' + user.lastname + " " + user.email
    data1 = {
        'solt': solt,
        'hash': hash,
        'user': request.user,
    }
    data = data | data1
    return render(request, 'users/user.html',context=data)
@login_required
@permission_edit_required('users.user_delete')
def user_delete(request, UsersID):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    user = User.objects.select_related().get(pk=UsersID)
    user.delete()
    return redirect('users:Users_all')
@login_required
@permission_edit_required('users.user_all')
def users_search(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    arg = request.GET.get('search')
    data = get_search(User,arg)
    return render(request, 'RRIT/view_all.html',context=data)

@login_required
@permission_edit_required('users.position_add')
def users_positions_add(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('users:Positions_id', obj.pk)
    else:
        data = get_settings(Positions)
        form = PositionForm()
    data['action_model'] = 'Positions'
    data1 = {
            'form': form,
        }
    data = data | data1

    return render(request, 'Incidents/add_specification.html', context=data )
@login_required
@permission_edit_required('users.position_all')
def users_positions_search(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    arg = request.GET.get('search')
    data = get_search(Positions, arg, 1)
    data['action_model'] = 'Positions'
    return render(request, 'RRIT/view_all.html',context=data)
@login_required
@permission_edit_required('users.position_all')
def users_positions(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    data = get_settings(Positions,1)
    data['action_models_s'] = 'Position'
    data['action_model'] = 'Positions'
    data1 = {
        'start_model': 'users',
        'add': 'add/'
    }
    data = data | data1
    return render(request, 'RRIT/view_all.html',context=data)


@login_required
@permission_edit_required('users.position_id')
def users_positions_id(request, PositionID):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    position = Positions.objects.select_related().get(pk=PositionID)

    data = get_settings(Positions)
    data['action_model'] = 'Positions'
    data1 = {
        'position':position,
    }
    data = data | data1
    return render(request, 'Position/id_position.html',context=data)
@login_required
@permission_edit_required('users.position_change')
def users_positions_change(request, PositionID):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    position = Positions.objects.select_related().get(pk=PositionID)
    if request.method == 'POST':
        form = PositionForm(request.POST, instance=position)
        if form.is_valid():
            obj = form.save()
            return redirect('users:Positions_id', obj.pk)
    else:
        form = PositionForm()
        form.fields['positions'].widget.attrs['value'] = position.positions

    data = get_settings(Positions)
    data['action_model'] = 'Positions'
    data1 = {
        'form': form,
        'position': position,
    }
    data = data | data1
    return render(request, 'Position/change_position.html', context=data)
@login_required
@permission_edit_required('users.position_delete')
def users_positions_delete(request, PositionID):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    position = Positions.objects.get(pk=PositionID)
    position.delete()
    return redirect('users:users_positions')
def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница users не найдена')


