from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import render, redirect
from Graduation_Work_With_Django import settings
from django.apps import apps

all_models = []
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
def get_sidebar():
    list1 = apps.get_models()
    app_models = []
    #есть список моделей
    for model1 in list1:
        if model1._meta.app_label == 'Incidents' or model1._meta.app_label == 'users' or model1._meta.app_label == 'Subdivisions':
            array_of_permissions = [list(row) for row in model1._meta.permissions]
            for value in array_of_permissions:
                value[0] = model1._meta.app_label + '.' + value[0]
            help_array = []
            for model in list1:
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

def get_settings(model, sql=None):
    app_models = get_sidebar()

    if sql:
        if model._meta.object_name == 'Incidents':
            Model_all = model.objects.all().order_by('-time_create').select_related()
        else:
            Model_all = model.objects.all().select_related()

    function_name = 'views_all'
    action_model = model._meta.app_label
    action_models_s = model._meta.app_label[:-1]
    eddit_name = model._meta.app_label
    breadcrumb_ru = model._meta.app_label
    ru_name_single = model._meta.verbose_name
    ru_name_all = model._meta.verbose_name_plural
    array_of_th = []
    array_of_data = []
    for i in range(len(model.list_display)):
        array_of_th.append(model._meta.get_field(model.list_display[i]).verbose_name)
    if 'Model_all' in locals():
        for data in Model_all:
            help_array = []
            for list in data.list_display:
                help_array.append({
                    list: getattr(data, list),
                })

            array_of_data.append({
                data.id: help_array,
            })
    data = {
        'ru_name_single':ru_name_single,
        'ru_name_all':ru_name_all,
        'function_name': function_name,
        'breadcrumb_ru': breadcrumb_ru,
        'action_model': action_model,
        'action_models_s': action_models_s,
        'eddit_name': eddit_name,
        'array_of_th': array_of_th,
        'app_models':app_models,
    }
    if array_of_data:
        data1 = {
            'array_of_data': array_of_data,
        }
        data = data | data1
    return data

def get_search(model, arg, sql=None):
    if model._meta.object_name == 'User':
        filter_model = model.objects.filter(
            Q(email__icontains=arg) | Q(name__icontains=arg) | Q(surname__icontains=arg) | Q(lastname__icontains=arg))
    elif model._meta.object_name == 'Incidents':
        filter_model = model.objects.filter(
            Q(address__icontains=arg) | Q(description__icontains=arg) |Q(user_create__name=arg,user_create__surname=arg, user_create__lastname=arg, _connector=Q.OR) | Q(user_create__fullname__icontains=arg))
    elif model._meta.object_name == 'Specifications':
        filter_model = model.objects.filter(
            Q(pattern__icontains=arg) | Q(color__icontains=arg))
    elif model._meta.object_name == 'Positions':
        filter_model = model.objects.filter(
            Q(positions__icontains=arg))
    elif model._meta.object_name == 'Subdivisions':
        filter_model = model.objects.filter(
            Q(abbreviation__icontains=arg) | Q(description__icontains=arg) | Q(address__icontains=arg))
    elif model._meta.object_name == 'Status':
        filter_model = model.objects.filter(
            Q(status__icontains=arg) | Q(description__icontains=arg))

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

    data = get_settings(model, sql)
    data['array_of_data'] = array_of_data

    return data
@login_required
def index(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL)
    app_models = get_sidebar()
    # app_list = apps.get_models()
    return render(request, 'RRIT/index.html',
                  {'app_models': app_models,})



def handler403(request, exception):
    app_models = get_sidebar()
    return render(request, 'errors/403.html', {'app_models':app_models}, status=403)

