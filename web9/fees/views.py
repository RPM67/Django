from django.shortcuts import render

def showFees(request):
    return render(request,'fees/index.html')
