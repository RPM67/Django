from django.shortcuts import render
from .models import student_info

def show(request):
    student = student_info.objects.all()
    specific_student = student_info.objects.get(pk=1) # here we are passing a specific data from database 
                                                      # using get() whose using primary key of table.
    return render(request,'student/index.html',{'stu':student, 'spec_stu':specific_student})
