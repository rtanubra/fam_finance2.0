from django.urls import path
from . import views 
#{% url 'people:people_index' %}
app_name= 'categories'
urlpatterns= [
    #categories/1/
    path("<int:person_id>/",views.index, name='person_category_index'),
    path("<int:person_id>/newCategory/",views.addCategory,name="new_category")

]