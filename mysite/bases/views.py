from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def header(request):
    context = {}
    return render(request, "bases/header.html",context)