from django.contrib import admin
from .models import pathtest
from .models import customer
from .models import catalogue
from .models import *
from import_export.admin import ImportExportModelAdmin



admin.site.register(pathtest)
# Register your models here.

#@admin.register(customer)
#class ViewAdmin(ImportExportModelAdmin):
    #list_display = ('Customer_ID')
admin.site.register(customer)
@admin.register(catalogue)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ('objectID' , 'title', 'link', 'image_link')
@admin.register(purchases)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ('Customer_ID' , 'Products', 'Month')
