from django import template

#the below allows us to register this django 'filter'
register = template.Library()

#define the 'filter'
def subtract(value,arg):
    return value - arg

#register the filter
register.filter('subtract', subtract)