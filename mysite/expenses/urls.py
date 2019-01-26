from django.urls import path
from . import views 
#{% url 'people:people_index' %}
app_name= 'expenses'
urlpatterns= [
    #expenses/1/addExpense
    path("<int:person_id>/<int:category_id>/addExpense/",views.add_expense, name='add_expense'),
]