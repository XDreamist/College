from django.db import models

# Create your models here.

class Registration(models.Model):
    f_name = models.CharField(max_length=25)
    l_name = models.CharField(max_length=25)
    age = models.CharField(max_length=2)
    qual = models.CharField(max_length=25)
    sub = models.CharField(max_length=15)