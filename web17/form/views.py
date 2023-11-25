from django.shortcuts import render
from .forms import studentRegistration
# Create your views here.

def show(request):
    fm = studentRegistration()
    
    fm.order_fields(field_order=['name','mobile','email','course']) # it will rearrange the feilds in the sequence
                                                                    # of list you provide here in feild_order 
                                                                    # argument inside order_feilds method. if 
                                                                    # sequence not given here then the default
                                                                    # order in which feild are created in forms.py
                                                                    # file will be followed.
                                                            
    
    return render(request,'form/index.html',{'form':fm})

