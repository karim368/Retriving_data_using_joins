from django.contrib import admin

# Register your models here.

from app.models import *
class Customization(admin.ModelAdmin):
    list_display = ['dname']
class Cust(admin.ModelAdmin):
    list_display = ['ename']
class Custom(admin.ModelAdmin):
    list_display = ['grade']
admin.site.register(Dept,Customization)
admin.site.register(Emp,Cust)
admin.site.register(SalGrade,Custom)