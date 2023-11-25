from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import student_info

def show(request):
    student = student_info.objects.all()

    return render(request,'student/index.html',{'stu':student})
