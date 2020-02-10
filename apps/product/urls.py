from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    path('', shop_page, name='product_list')
]
