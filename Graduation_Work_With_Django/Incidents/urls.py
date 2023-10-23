from django.urls import path

from .views import *

urlpatterns = [
    path('', incidents_all, name='Incidents_all'),  # http://127.0.0.1:8000/Incidents - Incidents из мейн файла urls
    path('<int:IncidentId>/change/', incidents_id, name='Incidents_ID'),  # http://127.0.0.1:8000/Incidents/id/
    path('?', incidents_search, name='Incidents_search'),
]
