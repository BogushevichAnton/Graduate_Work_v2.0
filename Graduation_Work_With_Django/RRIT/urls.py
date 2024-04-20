from django.urls import path

from users.views import login_user
from .views import *

urlpatterns = [
    path('', index, name='home'),
]