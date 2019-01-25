from django.db import models

# Create your models here.
class Group(models.Model):
    def __str__(self):
        return self.group_name
    group_name = models.CharField(max_length=200,unique=True)
    group_location = models.CharField(max_length=200, default= "Mississauga")