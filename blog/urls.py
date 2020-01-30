from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', list_blog, name='blog_list'),
    path('<id>/', detail_blog, name='blog_detail')
]