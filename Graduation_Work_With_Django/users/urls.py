from django.urls import path

from .views import *

app_name = "users"

urlpatterns = [
    path('login/', login_user, name='login'),  # http://127.0.0.1:8000/Incidents/id/
    path('logout/', logout_user, name='logout'),  # http://127.0.0.1:8000/Incidents/id/
    path('', users_all, name='Users_all'),  # http://127.0.0.1:8000/Incidents - Users из мейн файла urls

    path('Position/', users_positions, name='users_positions'),  # http://127.0.0.1:8000/Incidents - Users из мейн файла urls
    path('Position/?', users_positions_search, name='Positions_search'),
    path('Position/<int:PositionID>/', users_positions_id, name='Positions_id'),
    path('Position/add/', users_positions_add, name='Positions_add'),
    path('Position/<int:PositionID>/change/', users_positions_change, name='Positions_change'),
    path('Position/<int:PositionID>/delete/', users_positions_delete, name='Positions_delete'),

    path('<int:UsersID>/', user_id, name='User_ID'),  # http://127.0.0.1:8000/Incidents/id/
    path('<int:UsersID>/delete/', user_delete, name='user_delete'),  # http://127.0.0.1:8000/Incidents/id/
    path('?', users_search, name='Users_search'),
]
