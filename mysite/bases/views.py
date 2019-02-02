from django.shortcuts import render,redirect,get_object_or_404, get_list_or_404
from django.http import HttpResponse,HttpResponseRedirect

from people.models import People
from groups.models import Group 
import datetime
# Create your views here.

def landing(request):
    print(request.user)
    if request.user.is_authenticated:
        today = datetime.date.today()
        current_user = get_object_or_404(People,username=request.user)
        context = {
            'this_month':today.month,
            'this_year':today.year,
            'current_user':current_user
        }
        return render(request,'bases/landing_page.html',context)
    else:
        context = {} 
        return render(request,'bases/landing_request_login.html',context)