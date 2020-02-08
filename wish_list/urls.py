from django.urls import path
from .views import *

app_name = 'wishlist'

urlpatterns = [
    path('', get_items, name='product_list')
]

