from django.db import models

class details(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=50)
    
    course = models.CharField(max_length=30, default='BCA') # this feild name is an add on in this table after 
                                                            # we succesfully migrated this model with above 
                                                            # feilds.for add-on in the model, we have to provide
                                                            # the default value like this field here otherwise
                                                            # it will ask the values in terminal and things will
                                                            # get complicated and it will be difficult to run 
                                                            # migrate command. 
