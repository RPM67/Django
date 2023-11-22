from django.contrib import admin
from .models import course_list

@admin.register(course_list)
class course_list_Admin(admin.ModelAdmin):
    list_display = ('Id','Name','Duration','Seats','Fees')
