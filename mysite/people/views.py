from django.shortcuts import render, get_object_or_404,get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect

from groups.models import Group
from .models import People
from .forms import PersonAddForm

# Create your views here.
def index(request):
    people = People.objects.all()
    context = {
        'people':people
    }
    return render(request, "people/index.html" ,context)

def create_person(request):
    group = Group.objects.get(id=1)
    initial_data = {
        'group_couple' : group
    }
    form = PersonAddForm(request.POST or None,initial=initial_data)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            form = PersonAddForm()
        else:
            print("Something happend!")
            form = PersonAddForm()
    context= {
        'form':form
    }
    return render(request,'people/create_person.html',context)

def edit_person(request,person_id):
    person = People.objects.get(id=person_id)
    form = PersonAddForm(request.POST or None,instance=person)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            form = PersonAddForm()
        else:
            print("Something happend!")
            form = PersonAddForm()
    context = {
        'form':form
    }
    return render(request,'people/edit_person.html',context)