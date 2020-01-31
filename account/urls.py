from django.urls import path, include

app_name = 'account'

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken'))
]