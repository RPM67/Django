from django.contrib import admin
from student.models import student_info
# Register your models here.

# if wanna show single column data with any 1 feild name as that column in 
# admin-interface then just register your models in admin.py file and define 
# __str__ method with your choosen feild name in model class.(see 'web14' project)

# if wanna show complete table in admin-interface then just define a model admin
# class and use your required model admin option like list_display and register 
# the model admin class in admin.py file and you are done.(see 'web15' project)


@admin.register(student_info) # it automatically registers the below model admin class 
                              # with model class provided as argument in it to show 
                              # complete table in admin-interface. if multiple model 
                              # classes use this below model admin class then write it
                              # in decorator arguments by giving comma.
class student_info_Admin(admin.ModelAdmin):
    list_display = ('id','name','roll','course')
    
    
# admin.site.register(student_info,student_info_Admin)  # you can either use this statement to register your
                                                        # model admin class or the decorator used above. do as
                                                        # per your need and convinience