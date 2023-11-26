from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import studentRegistration
# Create your views here.
def success(request):
    return render(request,'form/success.html')
def show(request):
    if request.method == 'POST': # when form opens 1st time then by default GET request done and when submit button clicked then POST method runs
        fm = studentRegistration(request.POST) # we are passing the url or raw data came from POST request method into the form
        if fm.is_valid():
            print('Form Validated Successfully') # see terminal below
            print(f"Name : {fm.cleaned_data['name']}")
            print(f"Mobile : {fm.cleaned_data['mobile']}")
            print(f"Email : {fm.cleaned_data['email']}")
            print(f"Course : {fm.cleaned_data['course']}")
          #  return HttpResponseRedirect('/success/') # must provide the complete url where you wanna redirect after submitting form.
            return redirect('successPage') # in this case, can provide both url name and complete url too.
    else:
        fm = studentRegistration() 
                                                            
    return render(request,'form/index.html',{'form':fm})

