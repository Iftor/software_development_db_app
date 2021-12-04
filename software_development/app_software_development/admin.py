from django.contrib import admin
from django.db.models import fields
from . import models


@admin.register(models.ProgrammingLanguage)
class ProgrammingLanguageAdmin(admin.ModelAdmin):
    list_display = ['id', 'programming_language_name']
    list_filter = ['programming_language_name']


@admin.register(models.PersonalityFile)
class PersonalityFileAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'lastname', 'email']
    list_filter = ['firstname', 'lastname'] 


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'orders_number', 'personality_file']
    list_filter = ['orders_number']


@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'personality_file', 'salary']
    list_filter = ['salary']


@admin.register(models.Tester)
class TesterAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee', 'programming_language']
    list_filter = ['programming_language']


@admin.register(models.Programmer)
class ProgrammerAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee', 'programming_language']
    list_filter = ['programming_language']


@admin.register(models.Teamlead)
class TeamleadAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee']


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'required_programming_language', 'receiving_date', 'deadline']
    list_filter = ['required_programming_language']


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'teamlead', 'programming_language', 'order', 'beginning_date', 'ending_date']
    list_filter = ['programming_language']
