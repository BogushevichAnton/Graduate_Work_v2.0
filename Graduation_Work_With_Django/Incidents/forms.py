from django import forms
from django.core.exceptions import ValidationError

from .models import Incidents, Specifications


class AddIncidentsForm(forms.ModelForm):
    specification = forms.ModelChoiceField(queryset=Specifications.objects.all(),
                                           widget=forms.Select(attrs={'class': 'form-select mt-1',
                                                                      'style': 'height: 100%;',
                                                                      'id': 'select',
                                                                      }), initial=1)

    class Meta:
        model = Incidents
        fields = '__all__'
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control',
                                              'id': 'address',
                                              'placeholder': 'Адрес',
                                              'maxlength': '250',
                                              'readonly': 'readonly',
                                              'type': '',
                                              'value':'',
                                              }
                                       ),
            'description': forms.Textarea(attrs={'class': 'form-control mt-1',
                                                 'id': 'exampleFormControlTextarea1',
                                                 'rows': '4',
                                                 'style': 'resize:none; font-size: 1rem; font-weight: 400; line-height: 1.5;',
                                                 'placeholder': 'Описание инцидента',
                                                 'maxlength': '250',
                                                 },
                                          ),

            'latitude': forms.TextInput(attrs={'class': 'form-control',
                                               'type': '',
                                               'id': 'lat',
                                               'placeholder': 'Широта',
                                               'readonly': 'readonly',
                                               'value': '',
                                               }),
            'longitude': forms.TextInput(attrs={'class': 'form-control',
                                                'type': '',
                                                'id': 'lng',
                                                'placeholder': 'Долгота',
                                                'readonly': 'readonly',
                                                'value': '',
                                                }),
        }
        labels = {
            'description': '',
            'latitude': '',
            'longitude': '',
        }
        error_messages = {
            'address': {
                'max_length': "Максимальное количество символов - 250.",
                'required': "Обязательное поле - Адрес. Для его ввода необходимо поставить метку на карте."
            },
            'latitude': {
                'required': "Обязательное поле - Широта. Для его ввода необходимо поставить метку на карте.",
            },
            'longitude': {
                'required': "Обязательное поле - Долгота. Для его ввода необходимо поставить метку на карте.",
            },
            'description': {
                'max_length': "Максимальное количество символов - 250.",
                'required': "Обязательное поле - Описание."
            },
        }



class AddSpecificationsForm(forms.ModelForm):
    class Meta:
        model = Specifications
        fields = '__all__'
        widgets = {
            'pattern': forms.TextInput(attrs={
                                              'placeholder': 'Характеристика инцидента',
                                              'maxlength': '100',
                                                'class': 'vTextField',
                                              }
                                       ),
            'color': forms.TextInput(attrs={
                                              'placeholder': 'Цвет',
                                              'maxlength': '20',
                'class': 'vTextField',
                                              }
                                       ),
        }
        labels = {
        }
        error_messages = {
            'pattern': {
                'max_length': "Максимальное количество символов - 100.",
                'required': "Обязательное поле - Описание."
            },
            'color': {
                'max_length': "Максимальное количество символов - 20.",
                'required': "Обязательное поле - Цвет."
            },
        }
