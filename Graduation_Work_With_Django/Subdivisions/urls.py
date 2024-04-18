from django.urls import path

from .views import *

urlpatterns = [
    path('Subdivision/', subdivisions_all, name='Subdivisions_all'),  # http://127.0.0.1:8000/Subdisions - Subdisions из мейн файла urls
    path('Subdivision/<int:Subdivision_ID>/', subdivision_id, name='Subdivision_ID'),  # http://127.0.0.1:8000/Subdisions/Subdivision/id/
    path('Subdivision/map/', subdivisions_map, name='Subdivision_map'),
    path('Subdivision/add/', subdivisions_add, name='Subdivision_add'),

    path('Subdivision/<int:Subdivision_ID>/change/', subdivision_change, name='Subdivision_change'),
    path('Subdivision/<int:Subdivision_ID>/delete/', subdivision_delete, name='Subdivision_delete'),
    # http://127.0.0.1:8000/Subdisions/Subdivision/id/
    #path('Subdivision/<int:SubdivisionId>/change/', subdivision_change, name='Subdivision_delete'),
    # http://127.0.0.1:8000/Incidents/id/change
    #path('Subdivision/<int:SubdivisionId>/delete/', subdivision_delete, name='Subdivision_change'),
    # http://127.0.0.1:8000/Incidents/id/delete
]
