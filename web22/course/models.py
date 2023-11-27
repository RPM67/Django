from django.db import models

# Create your models here.
class data(models.Model):
    course_id = models.IntegerField(primary_key=True)
    course_name = models.CharField(max_length=40)
