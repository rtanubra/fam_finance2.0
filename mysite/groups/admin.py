from django.contrib import admin

from .models import Group
from people.models import People
from categories.models import Category
# Register your models here.

admin.site.register(Group)
admin.site.register(People)
admin.site.register(Category)