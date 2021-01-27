from django.contrib import admin
from .models import *
class employeeAdmin(admin.ModelAdmin):
    search_fields = ['Name']
class odczytAdmin(admin.ModelAdmin):
    search_fields = ['nr_karty']
# Register your models here.
admin.site.register(employee, employeeAdmin)
admin.site.register(odczyt, odczytAdmin)
