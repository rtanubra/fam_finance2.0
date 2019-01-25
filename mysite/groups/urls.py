from django.urls import path
from . import views 

app_name= 'groups'

urlpatterns= [
    #groups
    path("",views.index,name='groups_index'),
    path("newgroup/",views.create_group, name='create_group'),
    path("<int:my_id>/",views.inspect_group, name='inspect_group'),
]