from django.contrib import admin
from .models import student
# Register your models here.

@admin.register(student)
class data_Admin(admin.ModelAdmin):
    list_display = ('roll','name')
    