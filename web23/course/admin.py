from django.contrib import admin
from .models import data

# Register your models here.

@admin.register(data)
class data_Admin(admin.ModelAdmin):
    list_display = ('course_id','course_name','course_pass')