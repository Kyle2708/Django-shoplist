from django.db import models
from django.utils import timezone
import datetime
from django_pandas.io import read_frame
from django_pandas.managers import DataFrameManager
import pandas as pd 

# Create your models here.


class pathtest(models.Model):    
    product = models.CharField(max_length=100)
    path = models.URLField(max_length=500)

    def __str__(self):
        return self.product
   
class customer(models.Model):
    Customer_ID = models.IntegerField(default=0)

    def __str__(self):
        template = '{0.Customer_ID}'
        return template.format(self)
        
class purchases(models.Model):
    Customer_ID = models.IntegerField(default=0)
    Products = models.CharField(max_length=20)
    Month = models.DateTimeField()

    def __str__(self):
        template = '{0.Customer_ID} {0.Products} {0.Month}'
        return template.format(self)

class catalogue(models.Model):
    objectID = models.TextField(max_length=100)
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=500)
    image_link = models.URLField(max_length=500)

    def __str__(self):
        template = '{0.objectID} {0.title} {0.link} {0.image_link}'
        return template.format(self)