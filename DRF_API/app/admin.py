from django.contrib import admin
from .models import Employee
# Register your models here.

@admin.register(Employee)
class EMPAdmin(admin.ModelAdmin):
    list_display = ['Eid','Ename','Eloc','Ejob','Esal']