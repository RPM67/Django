from django.db import models

# if wanna show single column data with any 1 feild name as that column in 
# admin-interface then just register your models in admin.py file and define 
# __str__ method with your choosen feild name in model class.(see 'web14' project)

# if wanna show complete table in admin-interface then just define a model admin
# class and use your required model admin option like list_display and register 
# the model admin class in admin.py file and you are done.(see 'web15' project)


class student_info(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=70)
    course = models.CharField(max_length=30, default='BCA')
    
    def __str__(self): # used to represent any 1 feild as single column data in admin interface
        return str(self.roll) # it must return a string value to show in admin panel otherwise gives error. either 
                              # return any string value feild from above or convert the int value feild into 
                              # string type using str() method. 
