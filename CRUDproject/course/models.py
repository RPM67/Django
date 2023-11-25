from django.db import models

class course_list(models.Model):
    Id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=70)
    Duration = models.CharField(max_length=15)
    Seats = models.IntegerField()
    Fees = models.IntegerField()
    

