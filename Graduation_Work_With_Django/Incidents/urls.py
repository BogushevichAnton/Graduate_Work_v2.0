from django.urls import path

from .views import *

urlpatterns = [
    path('', incidents_all, name='Incidents_all'),  # http://127.0.0.1:8000/Incidents - Incidents из мейн файла urls
    path('<int:IncidentId>/', incidents_id, name='Incidents_ID'),  # http://127.0.0.1:8000/Incidents/id/
    path('<int:IncidentId>/change/', incidents_change, name='Incidents_change'),  # http://127.0.0.1:8000/Incidents/id/change
    path('<int:IncidentId>/delete/', incidents_delete, name='Incidents_delete'),    # http://127.0.0.1:8000/Incidents/id/delete

    path('?', incidents_search, name='Incidents_search'),
    path('add/', incidents_add, name='Incidents_add'),
    path('map/', incidents_map, name='Incidents_map'),


    path('Specification/', incidents_specification, name='Incidents_specification'),
    path('Specification/?', incidents_specification_search, name='Specification_search'),
    path('Specification/add/', incidents_specification_add, name='Incidents_specification_add'),
    path('Specification/<int:SpecificationsId>/', incidents_specification_id, name='Specification_ID'),
    path('Specification/<int:SpecificationsId>/change/', incidents_specification_change, name='Specification_change'),
    path('Specification/<int:SpecificationsId>/delete/', incidents_specification_delete, name='Specification_delete'),
]
handler404 = 'Incidents.views.pageNotFound'
