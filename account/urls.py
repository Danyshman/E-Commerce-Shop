from django.urls import path, include
from .views import *

app_name = 'account'

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('create/', create_user),
    path('login/', login_user)
]