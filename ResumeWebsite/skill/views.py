from django.shortcuts import render

def skill(request):
    context = {'skill':'activePage'}
    return render(request,'skill/skills.html',context)
