from django.urls import path

from .views import *

urlpatterns = [
    path('', UsersALL, name='Users_all'), #http://127.0.0.1:8000/Incidents - Users из мейн файла urls
    path('user/<int:UsersID>/', UsersID, name='User_ID'), #http://127.0.0.1:8000/Incidents/id/
]