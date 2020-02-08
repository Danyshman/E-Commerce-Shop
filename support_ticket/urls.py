from django.urls import path
from .views import ticket_list

app_name = 'support_ticket'

urlpatterns = [
    path('', ticket_list, name='ticket_list')
]