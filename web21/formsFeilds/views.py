from django.shortcuts import render,redirect
from .forms import differentFormFeilds
# Create your views here.

def success(request):
    return render(request,'formsFeilds/success.html')

def show(request):
    if request.method == 'POST':
        fm = differentFormFeilds(request.POST)
        if fm.is_valid():
            print('Form Validated Successfully')
            print(fm.cleaned_data['name'])
            print(fm.cleaned_data['roll'])
            print(fm.cleaned_data['height1'])
            print(fm.cleaned_data['height2'])
            print(fm.cleaned_data['url'])
            print(fm.cleaned_data['date'])
            print(fm.cleaned_data['time'])
            print(fm.cleaned_data['dateTime'])
            print(fm.cleaned_data['duration'])
            print(fm.cleaned_data['file'])
            print(fm.cleaned_data['filepath'])
            print(fm.cleaned_data['image'])
            print(fm.cleaned_data['choice'])
            print(fm.cleaned_data['multiChoice'])
            print(fm.cleaned_data['nullBoolean'])
            print(fm.cleaned_data['textarea'])
            print(fm.cleaned_data['password'])
            print(fm.cleaned_data['agree'])
            
            return redirect('successPage')
    else:
        fm = differentFormFeilds()
        
    return render(request,'formsFeilds/index.html',{'form':fm})