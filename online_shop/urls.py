"""online_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from product.views import index, about_us, contacts


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('products/', include('product.urls')),
    path('blogs/', include('blog.urls')),
    path('about-us/', about_us, name='about_us'),
    path('user/', include('account.urls')),
    path('contacts/', contacts, name='contacts'),
    path('user/<user_id>/support-tickets/', include('support_ticket.urls'), name='support_ticket'),
    path('user/<user_id>/orders/', include('order.urls'), name='orders'),
    path('user/<user_id>/wishlist/', include('wish_list.urls'), name='wishlist')
]
