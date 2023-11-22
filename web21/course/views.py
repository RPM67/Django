from django.shortcuts import render, redirect
from .models import course_list
from .forms import courseRegistration

def homePage(request):
    return render(request,'course/home.html')

def showCourseDetails(request):
    db = course_list.objects.all()
    return render(request,'course/courseDetails.html',{'courses':db})

def coursesRegistration(request):
    if request.method == 'POST':
        
            fm = courseRegistration(request.POST)
            if fm.is_valid():
                nm = fm.cleaned_data['Name']
                du = fm.cleaned_data['Duration']
                id = fm.cleaned_data['Id']
                st = fm.cleaned_data['Seats']
                fs = fm.cleaned_data['Fees']
                reg = course_list(Name=nm, Duration=du, Id=id, Seats=st, Fees=fs)
                reg.save()
                if 'submit' in request.POST:
                    return redirect('courses')
                elif 'reset' in request.POST:
                    fm = courseRegistration(label_suffix=' ')
    else:
        fm = courseRegistration(label_suffix=' ')
    return render(request,'course/courseRegistration.html',{'form':fm})




def update_course(request, id):
    
    course = course_list.objects.get(pk=id)
    if request.method == 'POST':
        fm = courseRegistration(request.POST)
        fm.fields['Id'].disabled = True
        fm.fields['Id'].initial = course.Id
        if fm.is_valid():
            nm = fm.cleaned_data['Name']
            du = fm.cleaned_data['Duration']
            st = fm.cleaned_data['Seats']
            fs = fm.cleaned_data['Fees']
            
            course.Name = nm
            course.Duration = du
            course.Seats = st
            course.Fees = fs
            print(fm.cleaned_data)
            course.save()
            
            return redirect('courses')
            
    else:
        initial_values = {
            'Name':course.Name,
            'Id':course.Id,
            'Duration':course.Duration,
            'Seats':course.Seats,
            'Fees':course.Fees,
            }
        fm = courseRegistration(initial=initial_values)
        fm.fields['Id'].disabled = True
        
    return render(request, 'course/update_course.html', {'form': fm})


def delete_course(request,id):
        course = course_list.objects.get(pk=id)
        course.delete()
        return redirect('courses')
