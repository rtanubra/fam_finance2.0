from django.shortcuts import render, get_object_or_404,get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import Group
from people.models import People
from .forms import GroupAddForm
import datetime

# Create your views here.
def index(request):
    current_groups = Group.objects.all()
    current_user = current_user = get_object_or_404(People, username=request.user)
    context = {
        'current_groups':current_groups,
        'current_user':current_user
    }
    today = datetime.datetime.today()
    context["this_month"] = today.month
    context["this_year"] = today.year
    return render(request,'groups/index.html',context)

def create_group(request):
    initial_data={

    }
    form = GroupAddForm(request.POST or None,initial=initial_data)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            form = GroupAddForm()
        else:
            print("Something happend!")
            form = GroupAddForm()
    current_user = current_user = get_object_or_404(People, username=request.user)
    context= {
        'form':form,
        'current_user':current_user
    }
    today = datetime.datetime.today()
    context["this_month"] = today.month
    context["this_year"] = today.year
    return render(request,'groups/create_group.html',context)

def inspect_group(request,my_id):
    obj = get_object_or_404(Group, id=my_id)
    if len(obj.people_set.all())>=1:
        people = get_list_or_404(People,group_couple=obj)
    else:
        people = []
    form = GroupAddForm(request.POST or None, instance = obj)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            form = GroupAddForm(instance=obj)
        else:
            print("Something happend!")
            form = GroupAddForm(instance=obj)
    today = datetime.datetime.today()
    current_user = current_user = get_object_or_404(People, username=request.user)
    context = {
        'form':form,
        'group':obj,
        'people':people,
        'month':today.month,
        'year': today.year,
        'current_user':current_user
    }
    today = datetime.datetime.today()
    context["this_month"] = today.month
    context["this_year"] = today.year
    return render(request,'groups/inspect_group.html',context)