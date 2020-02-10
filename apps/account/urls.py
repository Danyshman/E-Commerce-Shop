from django.urls import path
from .views import *

app_name = 'account'

urlpatterns = [
    path('create/', create, name='create'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('<user_id>/profile/', user_profile, name='user_profile'),
    path('<user_id>/wishlist/', wishlist, name='user_wishlist')
]