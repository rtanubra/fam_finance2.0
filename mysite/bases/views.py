from django.shortcuts import render,redirect,get_object_or_404, get_list_or_404
from django.http import HttpResponse,HttpResponseRedirect

from people.models import People
from groups.models import Group 
import datetime
# Create your views here.

