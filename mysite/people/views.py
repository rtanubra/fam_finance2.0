from django.shortcuts import render, get_object_or_404,get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect

from groups.models import Group
from .models import People
#from .forms import GroupAddForm

# Create your views here.
def index(request):
    people = People.objects.all()
    context = {
        'people':people
    }
    return render(request, "people/index.html" ,context)