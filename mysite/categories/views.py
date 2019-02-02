from django.shortcuts import render, redirect,get_object_or_404,get_list_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect

#MODELS
from groups.models import Group
from people.models import People
from .models import Category

#FORMS
from .forms import CategoryAddForm

import datetime
#==================Helper Functions#==================
def calculate_summary(categories):
    expected = 0
    spent = 0
    left = 0
    for category in categories:
        expected += category.category_expected
        spent += category.category_spent
    left = expected-spent
    return expected, spent, left

#==================Application level views#==================
def index(request,person_id,month,year):
    if request.user.is_authenticated:
        person = get_object_or_404(People, id=person_id)
        group = get_object_or_404(Group,id=person.group_couple.id)
        all_people = get_list_or_404(People,group_couple=group)
        if len(all_people) > 1:
            other_members = [ peep for peep in all_people if peep != person ]
        else:
            other_members = []
        if len(person.category_set.filter(category_date__month=month,category_date__year=year))>=1:
            categories= get_list_or_404(Category,category_person=person,category_date__month=month,category_date__year=year)
        else:
            categories = []
        expected,spent,left = calculate_summary(categories)
        today = datetime.datetime.today()
        current_user = get_object_or_404(People, username=request.user)
        context = {
            'person':person,
            'categories':categories,
            'month':today.month,
            'year':today.year,
            'other_members':other_members,
            'expected': expected,
            'spent': spent,
            'left':left,
            "current_user":current_user
        }
        today = datetime.datetime.today()
        context["this_month"] = today.month
        context["this_year"] = today.year
        return render(request, "categories/index.html" ,context)
    else:
        context = {} 
        return render(request,'bases/landing_request_login.html',context)

#==================Views here#==================
def index_team(request,group_id,month,year):
    if request.user.is_authenticated:
        group = get_object_or_404(Group,id=group_id)
        all_people = get_list_or_404(People,group_couple=group)
        categories = []
        for person in all_people:
            if len(person.category_set.filter(category_date__month=month,category_date__year=year))>0:
                categories.extend(get_list_or_404(Category,category_person=person,category_date__month=month,category_date__year=year))

        expected,spent,left = calculate_summary(categories)
        today = datetime.datetime.today()
        current_user = get_object_or_404(People, username=request.user)
        context = {
            'categories':categories,
            'month':today.month,
            'year':today.year,
            'expected': expected,
            'spent': spent,
            'left':left,
            "current_user":current_user
        }
        today = datetime.datetime.today()
        context["this_month"] = today.month
        context["this_year"] = today.year
        return render(request, "categories/index_team.html" ,context)
    else:
        context = {} 
        return render(request,'bases/landing_request_login.html',context)

def index_person(request,person_id,month,year):
    if request.user.is_authenticated:
        person = get_object_or_404(People,id=person_id)
        if len(person.category_set.filter(category_date__month=month,category_date__year=year))>0:
            categories = get_list_or_404(Category, category_person=person, category_date__month=month,category_date__year=year)
        else:
            categories = []
        expected,spent,left = calculate_summary(categories)
        today = datetime.datetime.today()
        current_user = get_object_or_404(People, username=request.user)
        context = {
            'categories':categories,
            'month':today.month,
            'year':today.year,
            'expected': expected,
            'spent': spent,
            'left':left,
            "current_user":current_user
        }
        today = datetime.datetime.today()
        context["this_month"] = today.month
        context["this_year"] = today.year
        return render(request, "categories/index_person.html" ,context)
    else:
        context = {} 
        return render(request,'bases/landing_request_login.html',context)

def index_diff_month(request,person_id,month,year):
    if request.user.is_authenticated:
        person = get_object_or_404(People, id=person_id)
        if len(person.category_set.all())>=1:
            categories= get_list_or_404(Category,category_person=person,category_date__month=month,category_date__year=year)
        else:
            categories = []
        current_user = current_user = get_object_or_404(People, username=request.user)
        today = datetime.datetime.today()
        context = {
            'person':person,
            'categories':categories,
            'month':month,
            'year':year,
            "current_user":current_user
        }
        today = datetime.datetime.today()
        context["this_month"] = today.month
        context["this_year"] = today.year
        return render(request, "categories/index_person.html" ,context)
    else:
        context = {} 
        return render(request,'bases/landing_request_login.html',context)
    
def addCategory(request,person_id):
    if request.user.is_authenticated:
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
        today = datetime.datetime.today()
        current_user = current_user = get_object_or_404(People, username=request.user)
        context={
            "person":person,
            "form":form,
            'month':today.month,
            'year':today.year,
            'current_user':current_user
        }
        today = datetime.datetime.today()
        context["this_month"] = today.month
        context["this_year"] = today.year
        return render(request,"categories/new_category.html",context)
    else:
        context = {} 
        return render(request,'bases/landing_request_login.html',context)

def editCategory(request,person_id,category_id):
    if request.user.is_authenticated:
        person = get_object_or_404(People, id=person_id)
        category = get_object_or_404(Category, id=category_id)
        my_instance = category
        form = CategoryAddForm(request.POST or None,instance=my_instance,hide_condition=True)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                form = CategoryAddForm(instance=my_instance,hide_condition=True)
            else:
                print("Failed validation")
                form = CategoryAddForm(instance=my_instance,hide_condition=True)
        today = datetime.datetime.today()
        current_user = current_user = get_object_or_404(People, username=request.user)
        context = {
            'person':person,
            'category':category,
            'form':form,
            'month':today.month,
            'year':today.year,
            'current_user':current_user
        }
        today = datetime.datetime.today()
        context["this_month"] = today.month
        context["this_year"] = today.year
        return render(request,"categories/edit_category.html",context)
    else:
        context = {} 
        return render(request,'bases/landing_request_login.html',context)

def deleteCategory(request,person_id,category_id):
    if request.user.is_authenticated:
        person = get_object_or_404(People, id=person_id)
        category = get_object_or_404(Category, id=category_id)
        month = category.category_date.month
        year = category.category_date.year
        my_instance = category
        form = CategoryAddForm(request.POST or None,instance=my_instance,hide_condition=True)
        if request.method == "POST":
            if form.is_valid():
                obj = form.save(commit=False)
                obj.delete()
                return redirect(f"../../{month}_{year}")
    
        else:
            today = datetime.datetime.today()
            current_user = current_user = get_object_or_404(People, username=request.user)
            context = {
                'person':person,
                'category':category,
                'form':form,
                'month':today.month,
                'year':today.year,
                'current_user':current_user
            }
            today = datetime.datetime.today()
            context["this_month"] = today.month
            context["this_year"] = today.year
            return render(request,"categories/delete_category.html",context)
    else:
        context = {} 
        return render(request,'bases/landing_request_login.html',context)