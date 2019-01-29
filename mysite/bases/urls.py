from django.urls import path
from . import views

app_name= 'bases'
urlpatterns = [
    path("",views.header, name='header')
]