from django.urls import path, include
from .views import *
from order.views import *

app_name = 'account'

urlpatterns = [
    path('create/', create, name='create'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', user_profile, name='user_profile'),
    path('<user_id>/orders/', order_list, name='order_list')
]