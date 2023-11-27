from django.shortcuts import render,redirect
from .forms import studentDetails
from .models import student

# Create your views here.
def details(request):
    data = student.objects.all()
    if request.method == 'POST':
        fm = studentDetails(request.POST)
        if fm.is_valid():

            nm = fm.cleaned_data['name']
            rl = fm.cleaned_data['roll']
            
            reg = student(name = nm, roll = rl)
            reg.save()
            return redirect('homePage')
    else:
        fm = studentDetails()
    
    return render(request,'student/index.html',{'form':fm,'data':data})


    