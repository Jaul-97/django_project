from django.db import models
from django import forms

class EmpForm(forms.Form):
    id= forms.IntegerField()
    empname= forms.CharField(max_length=100)
    dept= forms.CharField(max_length=100)
    desg= forms.CharField(max_length=100)
    salary= forms.FloatField()

# Create your models here.
