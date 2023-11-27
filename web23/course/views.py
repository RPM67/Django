from django.shortcuts import render
from django.http import HttpResponse
from .forms import courseReg
from .models import data

# Create your views here.

def show(request):
    cor_data = data.objects.all()
    if request.method == 'POST':
        fm = courseReg(request.POST)
        if fm.is_valid():
            id = fm.cleaned_data['id']
            nm = fm.cleaned_data["name"]
            pw = fm.cleaned_data['password']
            print('course Id : ',id)
            print('course Name : ',nm)
            print('Password : ',pw)
            reg = data(course_id = id, course_name = nm, course_pass = pw)
            reg.save()
            return HttpResponse(f'<h1>{nm} course registered successfully</h1>')
    else:
        fm = courseReg()
    return render(request,'course/index.html',{'form':fm})