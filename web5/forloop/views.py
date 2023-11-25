from django.shortcuts import render

def ForLoop(request):
    student = ['rahul','rohit','aakash','kunal','rakesh']
    persons = {'per1':{'name':'rpm','age':20},
               'per2':{'name':'rakesh','age':10},
               'per3':{'name':'aakash','age':40},
               'per4':{'name':'kunal','age':50},
               'per5':{'name':'rohit','age':30},
               }
    return render(request,'forloop/index.html',{'stu':student,'persons':persons})
