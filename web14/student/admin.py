from django.contrib import admin

# if wanna show single column data with any 1 feild name as that column in 
# admin-interface then just register your models in admin.py file and define 
# __str__ method with your choosen feild name in model class.(see 'web14' project)

# if wanna show complete table in admin-interface then just define a model admin
# class and use your required model admin option like list_display and register 
# the model admin class in admin.py file and you are done.(see 'web15' project)

# Register your models here.

from student.models import student_info
admin.site.register(student_info)