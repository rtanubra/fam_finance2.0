from django.urls import path
from . import views 
#{% url 'people:people_index' %}
app_name= 'categories'
urlpatterns= [
    #categories/1/
    path("<int:person_id>/<int:month>_<int:year>/",views.index, name='person_category_index'),
    #categories/1/newCategory/
    path("<int:person_id>/newCategory/",views.addCategory,name="new_category"),
    #categories/1/editCategory/2/
    path("<int:person_id>/editCategory/<int:category_id>/",views.editCategory,name="edit_category"),
    #categories/1/deleteCategory/2/
    path("<int:person_id>/deleteCategory/<int:category_id>/",views.deleteCategory,name='delete_category'),
    #categories/group/1/
    path("group/<int:group_id>/<int:month>_<int:year>/",views.index_team , name="team_category_index"),
    path("person/<int:person_id>/<int:month>_<int:year>/",views.index_person , name="person_category_index_summary"),

]