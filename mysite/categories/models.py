from django.db import models
from people.models import People
from groups.models import Group
import datetime

# Create your models here.
class Category(models.Model):
    def __str__(self):
        return f"{self.category_person.person_name} {self.category_name} {self.category_date.month}/{self.category_date.year}"
    def calculate_left(self,expected,spent):
        return expected-spent 
    category_person = models.ForeignKey(People, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=200)
    category_expected = models.DecimalField(max_digits=8,decimal_places=2)
    category_spent = models.DecimalField(max_digits=8,decimal_places=2,default=0)
    category_date = models.DateField(default=datetime.datetime.now)