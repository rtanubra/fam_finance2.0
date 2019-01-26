from django.db import models
from people.models import People
from groups.models import Group
from categories.models import Category
import datetime

# Create your models here.
class Expense(models.Model):
    def __str__(self):
        return self.expense_name
    expense_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    expense_amount = models.DecimalField(max_digits=8,decimal_places=2)
    expense_description = models.CharField(max_length=200)
    expense_date = models.DateField(default=datetime.datetime.now)
    
    credit_card = "Credit"
    debit_card = "Cash/Debit"
    pmtChoices = (
        (credit_card , "Credit"),(debit_card,"Cash/Debit" )
    )
        
    method_of_payment = models.CharField(
        choices = pmtChoices,
        default = debit_card,
        max_length = 11
    )