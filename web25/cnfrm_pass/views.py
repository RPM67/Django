from django.shortcuts import render,redirect
from .forms import passwordCheck
# Create your views here.

def show(request):
    if request.method == 'POST':
        fm = passwordCheck(request.POST)
        if fm.is_valid():
            pw = fm.cleaned_data['password']
            cnfrm_pw = fm.cleaned_data['confirm_password']
            print('Password : ',pw)
            print('Confirm Password : ', cnfrm_pw)
            if pw == cnfrm_pw:   
                return render(request,'cnfrm_pass/index.html',{'form':fm,'matched':True})
            else:
                fm.add_error('confirm_password', 'Passwords do not match.') # either use this method to give
            #     error or use clean() method in forms.py file. clean() method is suitable when the validation 
            #     logic involves multiple fields or is more complex.this method here is suitable for simple cases 
            #     where the validation logic is specific to the view and doesn't involve complex interactions
            #     between multiple fields.since you're checking if the passwords match, and it's a relatively
            #     straightforward validation so it is quite better here. If you prefer to keep the validation 
            #     logic within the form itself, the clean method is a good choice
    else:
        fm = passwordCheck()
    return render(request,'cnfrm_pass/index.html',{'form':fm})