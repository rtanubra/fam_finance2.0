from django.contrib import admin

from .models import Group
from people.models import People
# Register your models here.

admin.site.register(Group)
admin.site.register(People)