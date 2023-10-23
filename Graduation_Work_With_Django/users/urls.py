from django.urls import path

from .views import *

urlpatterns = [
    path('', users_all, name='Users_all'),  # http://127.0.0.1:8000/Incidents - Users из мейн файла urls
    path('<int:UsersID>/change/', user_id, name='User_ID'),  # http://127.0.0.1:8000/Incidents/id/
    path('?', users_search, name='Users_search'),
]
