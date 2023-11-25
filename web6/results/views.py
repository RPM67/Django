from django.shortcuts import render

def showResults(request):
    python = 91
    vb = 78
    numerical = 80
    software_eng = 76
    cnin = 81
    total = 500
    obtained = int(python+vb+numerical+software_eng+cnin)
    percent = (obtained/total)*100
    if obtained < 200:
        rslt = 'failed'
    else:
        rslt = 'passed'
    
    result_details = {'pymarks':python,'vbmarks':vb,'nmmarks':numerical,'cnmarks':cnin,'semarks':software_eng,'obmarks':obtained,'tmarks':total,'percent':percent,'result':rslt}
    return render(request,'results/index.html',result_details)
