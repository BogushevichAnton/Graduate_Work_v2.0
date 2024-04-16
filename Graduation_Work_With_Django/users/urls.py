from django.urls import path

from .views import *

app_name = "users"

urlpatterns = [
    path('login/', login_user, name='login'),  # http://127.0.0.1:8000/Incidents/id/
    path('logout/', logout_user, name='logout'),  # http://127.0.0.1:8000/Incidents/id/
    path('', users_all, name='Users_all'),  # http://127.0.0.1:8000/Incidents - Users из мейн файла urls
    path('<int:UsersID>/', user_id, name='User_ID'),  # http://127.0.0.1:8000/Incidents/id/
    path('<int:UsersID>/delete/', user_delete, name='user_delete'),  # http://127.0.0.1:8000/Incidents/id/
    path('?', users_search, name='Users_search'),
]
