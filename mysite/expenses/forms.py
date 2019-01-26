from django import forms
from categories.models import Category
from .models import Expense
from django.forms.widgets import HiddenInput

class ExpenseAddForm(forms.ModelForm):

    class Meta:
        model= Expense
        fields = [
            'expense_category',
            'expense_description',
            'expense_amount',
            'expense_date',
            'method_of_payment'
        ]
    
    def __init__(self,*args,**kwargs):
        hide_condition = kwargs.pop('hide_condition',None)
        super(ExpenseAddForm, self).__init__(*args, **kwargs)
        if hide_condition:
            self.fields["expense_category"].widget = HiddenInput()
