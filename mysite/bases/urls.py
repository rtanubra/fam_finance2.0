from django.urls import path
from . import views 
#{% url 'people:people_index' %}
app_name= 'bases'
urlpatterns= [
    path("",views.landing, name='landing')
]