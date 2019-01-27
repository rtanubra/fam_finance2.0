from django.contrib import admin

from .models import Group
from people.models import People
from categories.models import Category
from expenses.models import Expense
# Register your models here.

admin.site.register(Group)
admin.site.register(People)
admin.site.register(Category)
admin.site.register(Expense)