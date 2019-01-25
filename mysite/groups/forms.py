from django import forms
from .models import Group

class GroupAddForm(forms.ModelForm):
    class Meta:
        model= Group
        fields = [
            'group_name',
            'group_location'
        ]