from django.shortcuts import render
from .forms import studentRegistration
# Create your views here.

def show(request):
    fm = studentRegistration()
                                                            
    return render(request,'form/index.html',{'form':fm})

