from django import forms
from people.models import People
from .models import Category
from django.forms.widgets import HiddenInput
class CategoryAddForm(forms.ModelForm):

    class Meta:
        model= Category
        fields = [
            'category_person',
            'category_name',
            'category_expected',
            'category_spent',
            'category_date'
        ]
    
    def __init__(self,*args,**kwargs):
        hide_condition = kwargs.pop('hide_condition',None)
        super(CategoryAddForm, self).__init__(*args, **kwargs)
        if hide_condition:
            self.fields["category_person"].widget = HiddenInput()