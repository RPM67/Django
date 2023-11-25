from django.shortcuts import render

def contact(request):
    context = {'contact':'activePage'}
    return render(request,'contact/contact.html',context)
