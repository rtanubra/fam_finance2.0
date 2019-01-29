from django.shortcuts import render, get_object_or_404,get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect

from groups.models import Group
from .models import People
from .forms import PersonAddForm

import datetime
# Create your views here.
def index(request):
    people = People.objects.all()
    current_user = current_user = get_object_or_404(People, username=request.user)
    context = {
        'people':people,
        'current_user':current_user
    }
    today = datetime.datetime.today()
    context["this_month"] = today.month
    context["this_year"] = today.year
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
    current_user = current_user = get_object_or_404(People, username=request.user)
    context= {
        'form':form,
        'current_user':current_user
    }
    today = datetime.datetime.today()
    context["this_month"] = today.month
    context["this_year"] = today.year
    return render(request,'people/create_person.html',context)

def edit_person(request,my_id):
    person = People.objects.get(id=my_id)
    form = PersonAddForm(request.POST or None,instance=person)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            form = PersonAddForm(instance=person)
        else:
            print("Something happend!")
            form = PersonAddForm()
    today = datetime.datetime.today()
    current_user = current_user = get_object_or_404(People, username=request.user)
    context = {
        'form':form,
        'person':person,
        'month':today.month,
        'year':today.year,
        'current_user':current_user
    }
    today = datetime.datetime.today()
    context["this_month"] = today.month
    context["this_year"] = today.year
    return render(request,'people/edit_person.html',context)