from django.urls import path
from .views import detail_blog

app_name = 'blog'

urlpatterns = [
    path('<id>/', detail_blog, name='detail_blog')
]