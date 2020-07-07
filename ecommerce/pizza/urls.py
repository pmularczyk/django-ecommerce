from django.urls import path

from .views import home

app_name = 'pizza'

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
]