from django.shortcuts import render

def bca(request):
    corname = 'bca'
    return render(request,'courses/bca.html',{'cn':corname})

def mca(request):
    corname = 'mca'
    return render(request,'courses/mca.html',{'cn':corname})
