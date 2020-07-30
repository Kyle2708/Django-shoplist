from django.shortcuts import render

from .models import purchases
from .models import catalogue
from .models import pathtest
from .models import customer
import requests
import csv, io
# Create your views here.
from django.http import HttpResponse
from django.http import StreamingHttpResponse
from django_tables2.tables import Table
#from.resources import testResource
from django.views.generic import TemplateView, ListView
import pandas as pd
import numpy
from django_pandas.io import read_frame
from django.contrib.messages import constants
from django.contrib import messages


# Create your views here.
def access(request):
    if request.META.get('HTTP_REFERER') == get_list:
        # Do something...
        return render(request, "test.html")
    else:
        return render(request, "test.html")
        # Redirect...
def indexPage(request):
    #context={'a':'a'}
    customers = customer.objects.all    
    all_paths = pathtest.objects.all
    qs = pathtest.objects.all()    
    return render(request,'index.html',{'customer':customers,'pathtest':all_paths})
    
def index2(request):    
    all_paths = pathtest.objects.all
    df = read_frame(pathtest.objects.all())
    list1 = { "dataframe":df, 'pathtest':all_paths}        
    return render(request, "test.html", list1)
       

def get_test(request):    
    #choice = request.POST.get('fruit')
    all_paths = pathtest.objects.all
    df = read_frame(pathtest.objects.all())
    selected = df.loc[df['product'] == choice]    
    list1 = { "dataframe":selected, 'pathtest':all_paths} 
    if choice in df.values:
        return render(request, "test.html", list1)
    else:
        return render(request, "test.html", list1)
    
def get_list(request):
    custid = request.POST.get('custid')
    #history = purchases.objects.all    
    cust = customer.objects.all 
    customers = read_frame(customer.objects.all())     
    customers = customers['Customer_ID']
    custid = int(custid)
           
    if custid in customers.unique():
        #funtion
        df = read_frame(purchases.objects.all())        
        df = df.loc[df['Customer_ID'] == custid]
        array = df['Products'].astype(int)
        cat = read_frame(catalogue.objects.all())
        cat = cat.head(5)
        pd.to_numeric(cat['objectID'])
        display = cat.loc[cat['objectID'].isin(array)]
        #function
        list1 = { "dataframe": cat, "customers":cust}
        return render(request, "get_list.html", list1)             
    else:        
        messages.error(request, 'Please enter valid username')
        return render(request, "index.html")  