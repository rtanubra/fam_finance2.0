from django.shortcuts import render, get_object_or_404,get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect

#MODELS
from groups.models import Group
from people.models import People
from .models import Category

#FORMS
from .forms import CategoryAddForm

# Create your views here.
def index(request,person_id):
    person = get_object_or_404(People, id=person_id)
    if len(person.category_set.all())>=1:
        categories= get_list_or_404(Category,category_person=person)
    else:
        categories = []
    context = {
        'person':person,
        'categories':categories
    }
    return render(request, "categories/index.html" ,context)

def addCategory(request,person_id):
    person = get_object_or_404(People, id=person_id)
    initial_data = {
        'category_person' : person
    }
    form = CategoryAddForm(request.POST or None,initial=initial_data,hide_condition=True)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            form = CategoryAddForm(initial=initial_data,hide_condition=True)
        else:
            print("Something happend!")
            form = CategoryAddForm(initial=initial_data,hide_condition=True)
    context={
        "person":person,
        "form":form
    }
    return render(request,"categories/new_category.html",context)