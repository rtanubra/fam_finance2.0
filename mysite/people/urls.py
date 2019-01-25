from django.urls import path
from . import views 
#{% url 'people:people_index' %}
app_name= 'people'
urlpatterns= [
    #groups
    path("",views.index,name='people_index')
    #path("newperson/",views.create_person, name='create_person'),
    #path("<int:my_id>/",views.inspect_person, name='inspect_person'),
]