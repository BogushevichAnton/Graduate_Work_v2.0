from django.urls import path

from .views import *

urlpatterns = [
    path('', IncidentsALL, name='Incidents_all'),  # http://127.0.0.1:8000/Incidents - Incidents из мейн файла urls
    path('Incident/<int:IncidentId>/', IncidentsID, name='Incidents_ID'),  # http://127.0.0.1:8000/Incidents/id/
    path('?q=<str:Incidents_search>/', Incidents_Search, name='Incidents_search'),
]
