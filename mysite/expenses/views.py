from django.shortcuts import render, get_object_or_404,get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect

#MODELS
from groups.models import Group
from people.models import People
from categories.models import Category
from .models import Expense

#FORMS
from .forms import ExpenseAddForm

# Create your views here.
def add_expense(request,person_id,category_id):
    person = get_object_or_404(People,id=person_id)
    category = get_object_or_404(Category,id=category_id)
    cc = get_object_or_404(Category, category_person=person, category_name="credit_card")
    initial_data = {
        'expense_category':category,
    }
    form = ExpenseAddForm(request.POST or None,initial=initial_data,hide_condition=True)
    if request.method == "POST":
        if form.is_valid():
            new_expense = form.save() 
            #We are paying off credit card
            if category == cc:
                category.category_expected -= new_expense.expense_amount
                category.category_spent -= new_expense.expense_amount
                category.save()
            #Purchasing Actual Expense
            else:
#==========================pmt type == CC#==========================
                if new_expense.method_of_payment == "Credit":
                    cc.category_expected += new_expense.expense_amount
                    cc.category_spent += new_expense.expense_amount
                    category.category_spent += new_expense.expense_amount
                    cc.save()
                    category.save()
    #==========================pmt type == Debit/Cash#==========================
                else:
                    category.category_spent += new_expense.expense_amount
                    category.save()


            #Start a new when done.
            form = ExpenseAddForm(initial=initial_data,hide_condition=True)
        else:
            print("HELP")
            form = ExpenseAddForm(initial=initial_data,hide_condition=True)
    context = {
        'form':form,
        'category':category,
        'person':person
    }
    return render(request,'expenses/add_expense.html',context)

def category_expense_list(request,person_id,category_id):
    person = get_object_or_404(People, id=person_id)
    category = get_object_or_404(Category, id=category_id)
    expenses = get_list_or_404(Expense,expense_category=category )
    context = {
        'person':person,
        'category':category,
        'expenses':expenses
    }
    return render(request,"expenses/category_expense_detail.html" ,context)