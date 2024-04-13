from django import forms
from django.core.exceptions import ValidationError

from .models import Incidents, Specifications


class AddPostForm(forms.ModelForm):
    specification = forms.ModelChoiceField(queryset=Specifications.objects.all(),
                                           widget=forms.Select(attrs={'class': 'form-select mt-1',
                                                                      'style': 'height: 100%;',
                                                                      'id': 'select',
                                                                      }), initial=0)

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
                                               }),
            'longitude': forms.TextInput(attrs={'class': 'form-control',
                                                'type': '',
                                                'id': 'lng',
                                                'placeholder': 'Долгота',
                                                'readonly': 'readonly',
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
