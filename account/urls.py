from django.urls import path, include
from .views import *

app_name = 'account'

urlpatterns = [
    path('create/', create, name='create'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', user_profile, name='user_profile')
]