from django.urls import path

from .views import *

urlpatterns = [
    path('Subdivision/', subdivisions_all, name='Subdivisions_all'),  # http://127.0.0.1:8000/Subdisions - Incidents из мейн файла urls
]
