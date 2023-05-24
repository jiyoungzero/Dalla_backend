from django.urls import path
from .views import *

app_name = 'api'
urlpatterns = [
    path('menu/', menu, name = "menu"),
]