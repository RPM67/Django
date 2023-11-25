from django.shortcuts import render

def IfElse(request):
    return render(request,'ifelse/index.html',{'nm':'Django','du':'4 months'})
