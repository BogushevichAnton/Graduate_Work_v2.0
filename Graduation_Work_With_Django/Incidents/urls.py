from django.urls import path

from .views import *

urlpatterns = [
    path('', Incidents), #http://127.0.0.1:8000/Incidents - Incidents из мейн файла urls
    path('<int:IncidentId>/', IncidentsID), #http://127.0.0.1:8000/Incidents/id/
]