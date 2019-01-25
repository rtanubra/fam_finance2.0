from django import forms
from .models import People
from groups.models import Group

class PersonAddForm(forms.ModelForm):

    class Meta:
        model= People
        fields = [
            'group_couple',
            'person_name',
            'username'
        ]