from django.shortcuts import render

def showCourses(request):
    return render(request,'course/main.html',{'d':'Django'})
