from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    path('', index, name='index'),
    path('shop/', shop_page, name='shop_page')
]
