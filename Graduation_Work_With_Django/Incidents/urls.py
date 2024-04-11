from django.urls import path

from .views import *

urlpatterns = [
    path('Incident/', incidents_all, name='Incidents_all'),  # http://127.0.0.1:8000/Incidents - Incidents из мейн файла urls
    path('Incident/<int:IncidentId>/change/', incidents_id, name='Incidents_ID'),  # http://127.0.0.1:8000/Incidents/id/
    path('Incident/?', incidents_search, name='Incidents_search'),
    path('Incident/add/', incidents_add, name='Incidents_add'),
    path('Incident/map/', incidents_map, name='Incidents_map'),
    path('Specification/', incidents_specification, name='Incidents_specification'),
]
