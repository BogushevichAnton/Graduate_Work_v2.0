from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import context

from Graduation_Work_With_Django import settings
from Incidents.models import *
from users.models import *
from django.contrib import admin
from django.apps import apps

all_models = []
def get_sidebar():
    list = apps.get_models()
    app_models = []
    for model1 in list:
        if model1._meta.app_label == 'Incidents' or model1._meta.app_label == 'users' or model1._meta.app_label == 'Subdivisions':
            help_array = []
            for model in list:
                if model._meta.app_label == model1._meta.app_label:
                    if model._meta.object_name not in help_array:
                        if model._meta.app_label == 'Incidents' and model._meta.object_name == 'Incidents':
                            help_array.append({
                                'name': model._meta.verbose_name_plural,
                                'app_label': model._meta.object_name,
                                'url_view': '/' + model._meta.app_label + '/',
                                'add_url': '/' + model._meta.app_label + '/add/',
                                'change_url': '/' + model._meta.app_label + '/change/',
                            }
                            )
                        if model._meta.app_label == 'Incidents' and model._meta.object_name == 'Specifications':
                            help_array.append({
                                'name': model._meta.verbose_name_plural,
                                'app_label': model._meta.object_name,
                                'url_view': '/' + model._meta.app_label + '/' + model._meta.object_name[:-1] + '/',
                                'add_url': '/' + model._meta.app_label + '/' + model._meta.object_name[:-1] + '/' + 'add/',
                                'change_url': '/' + model._meta.app_label + '/' + model._meta.object_name[
                                                                                  :-1] + '/' + 'change/',
                            }
                            )
                        if model._meta.app_label == 'Incidents' and model._meta.object_name == 'Status':
                                help_array.append({
                                    'name': model._meta.verbose_name_plural,
                                    'app_label': model._meta.object_name,
                                    'url_view': '/' + model._meta.app_label + '/' + model._meta.object_name + '/',
                                    'add_url': '/' + model._meta.app_label + '/' + model._meta.object_name + '/' + 'add/',
                                    'change_url': '/' + model._meta.app_label + '/' + model._meta.object_name + '/' + 'change/',
                                })
                        if model._meta.app_label == 'users' and model._meta.object_name == 'User':
                                help_array.append({
                                    'name': model._meta.verbose_name_plural,
                                    'app_label': model._meta.app_label,
                                    'url_view': '/' + model._meta.app_label + '/',
                                    'add_url': '/' + model._meta.app_label + '/' +  'add/',
                                    'change_url': '/' + model._meta.app_label + '/' +  'change/',
                                }
                                )
                        if model._meta.app_label == 'users' and model._meta.object_name == 'Positions':
                                help_array.append({
                                    'name': model._meta.verbose_name_plural,
                                    'app_label': model._meta.object_name,
                                    'url_view': '/' + model._meta.app_label + '/' + model._meta.object_name[:-1] + '/',
                                    'add_url': '/' + model._meta.app_label + '/' + model._meta.object_name[:-1] + '/' + 'add/',
                                    'change_url': '/' + model._meta.app_label + '/' + model._meta.object_name[
                                                                                      :-1] + '/' + 'change/',
                                }
                                )
                        if model._meta.app_label == 'Subdivisions':
                                help_array.append({
                                    'name': model._meta.verbose_name_plural,
                                    'app_label': model._meta.object_name,
                                    'url_view': '/' + model._meta.app_label + '/',
                                    'add_url': '/' + model._meta.app_label + '/add/',
                                    'change_url': '/' + model._meta.app_label + '/change/',
                                })
            if {model1._meta.app_label:help_array} not in app_models:
                    app_models.append({model1._meta.app_label: help_array})



    # for model in list:
    #     if model._meta.app_label == 'Incidents' and model._meta.object_name == 'Incidents':
    #         app_models.append({
    #             'app_head':model._meta.app_label,
    #             'name': model._meta.verbose_name_plural,
    #             'app_label': model._meta.object_name,
    #             'url_view': '/' + model._meta.app_label + '/' + model._meta.object_name[:-1] + '/',
    #             'add_url': '/' + model._meta.app_label + '/' + model._meta.object_name[:-1] + '/' + 'add/',
    #             'change_url': '/' + model._meta.app_label + '/' + model._meta.object_name[:-1] + '/' + 'change/',
    #         }
    #         )
    #     if model._meta.app_label == 'Incidents' and model._meta.object_name == 'Status':
    #         app_models.append({
    #             'app_head': model._meta.app_label,
    #             'name': model._meta.verbose_name_plural,
    #             'app_label': model._meta.object_name,
    #             'url_view': '/' + model._meta.app_label + '/' + model._meta.object_name + '/',
    #             'add_url': '/' + model._meta.app_label + '/' + model._meta.object_name + '/' + 'add/',
    #             'change_url': '/' + model._meta.app_label + '/' + model._meta.object_name + '/' + 'change/',
    #         })
    #     if model._meta.app_label == 'users' and model._meta.object_name == 'User':
    #         app_models.append({
    #             'app_head': model._meta.app_label,
    #             'name': model._meta.verbose_name_plural,
    #             'app_label': model._meta.app_label,
    #             'url_view': '/' + model._meta.app_label + '/' + model._meta.app_label[:-1] + '/',
    #             'add_url': '/' + model._meta.app_label + '/' + model._meta.app_label[:-1] + '/' + 'add/',
    #             'change_url': '/' + model._meta.app_label + '/' + model._meta.app_label[:-1] + '/' + 'change/',
    #         }
    #         )
    #     if model._meta.app_label == 'users' and model._meta.object_name == 'Positions':
    #         app_models.append({
    #                 'app_head': model._meta.app_label,
    #                 'name': model._meta.verbose_name_plural,
    #                 'app_label': model._meta.object_name,
    #                 'url_view': '/' + model._meta.app_label + '/' + model._meta.object_name[:-1] + '/',
    #                 'add_url': '/' + model._meta.app_label + '/' + model._meta.object_name[:-1] + '/' + 'add/',
    #                 'change_url': '/' + model._meta.app_label + '/' + model._meta.object_name[:-1] + '/' + 'change/',
    #             }
    #         )
    #     if model._meta.app_label == 'Subdivisions':
    #         app_models.append({
    #             'app_head': model._meta.app_label,
    #             'name': model._meta.verbose_name_plural,
    #             'app_label': model._meta.object_name,
    #             'url_view': '/' + model._meta.app_label + '/' + model._meta.object_name[:-1] + '/',
    #             'add_url': '/' + model._meta.app_label + '/' + model._meta.object_name[:-1] + '/' + 'add/',
    #             'change_url': '/' + model._meta.app_label + '/' + model._meta.object_name[:-1] + '/' + 'change/',
    #         })

    return app_models

def get_settings(model):
    app_models = get_sidebar()
    if model._meta.object_name == 'Incidents':
        Model_all = model.objects.all().order_by('-time_create')
    else:
        Model_all = model.objects.all()

    function_name = 'views_all'
    action_model = Model_all.model._meta.app_label
    action_models_s = Model_all.model._meta.app_label[:-1]
    eddit_name = Model_all.model._meta.verbose_name
    breadcrumb_ru = Model_all.model._meta.verbose_name_plural
    array_of_th = []
    array_of_data = []
    for i in range(len(Model_all.model.list_display)):
        array_of_th.append(Model_all.model._meta.get_field(Model_all.model.list_display[i]).verbose_name)

    for data in Model_all:
        help_array = []
        for list in data.list_display:
            help_array.append({
                list: getattr(data, list),
            })

        array_of_data.append({
            data.id: help_array,
        })
    count = len(array_of_data)
    data = {
        'function_name': function_name,
        'breadcrumb_ru': breadcrumb_ru,
        'action_model': action_model,
        'action_models_s': action_models_s,
        'eddit_name': eddit_name,
        'array_of_data': array_of_data,
        'count': count,
        'array_of_th': array_of_th,
        'app_models':app_models,
    }
    return data

def get_search(model, arg):
    if model._meta.object_name == 'User':
        filter_model = model.objects.filter(
            Q(email__icontains=arg) | Q(name__icontains=arg) | Q(surname__icontains=arg) | Q(lastname__icontains=arg))
    elif model._meta.object_name == 'Incidents':
        filter_model = model.objects.filter(
            Q(address__icontains=arg) | Q(description__icontains=arg) |Q(user_create__name=arg,user_create__surname=arg, user_create__lastname=arg, _connector=Q.OR) | Q(user_create__fullname__icontains=arg))
    elif model._meta.object_name == 'Specifications':
        filter_model = model.objects.filter(
            Q(pattern__icontains=arg) | Q(color__icontains=arg))
    array_of_data = []


    for mod in filter_model:
        help_array = []
        for list in mod.list_display:
            help_array.append({
                list: getattr(mod, list),
            })
        array_of_data.append({
            mod.id: help_array,
        })

    data = get_settings(model)
    data['array_of_data'] = array_of_data

    return data

def index(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    app_models = get_sidebar()
    # app_list = apps.get_models()
    return render(request, 'RRIT/index.html',
                  {'app_models': app_models,})


def permission_edit_required(perm, login_url=None, raise_exception=True):
    def check_perms(user):
        if isinstance(perm, str):
            perms = (perm, )
        else:
            perms = perm
        if user.has_perms(perms):
            return True
        if raise_exception and user.pk:
            raise PermissionDenied
        return False
    return user_passes_test(check_perms, login_url=login_url)
