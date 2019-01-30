from django.db import models
from groups.models import Group

# Create your models here.
class People(models.Model):

    def __str__(self):
        return self.person_name

    group_couple = models.ForeignKey(Group,on_delete=models.CASCADE)
    person_name= models.CharField(max_length=70)
    username = models.CharField(max_length=70,unique=True)
