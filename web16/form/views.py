from django.shortcuts import render
from .forms import studentRegistration
# Create your views here.

def show(request):
    fm = studentRegistration()
    return render(request,'form/index.html',{'form':fm})


# auto id argument example 
def show2(request):
    fm = studentRegistration(auto_id='form_%s',
     label_suffix=' - ')                            # by setting auto_id=True, the 'for' inside label and 'id'
                                                    # inside input feild will be set as feild name which was
                                                    # previously 'id_feildName' by default.
                                           
                                           # by setting auto_id=False, the <label> tag will be removed from 
                                           # feild name and id attribute will be removed from input feild.
                                           
                                           # by setting auto_id='string', the form will treat it as
                                           # auto_id=True and do same thing what happend by setting auto_id=True. 
                                           
                                           # by setting auto_id='string_%s', the for attribute of label and id
                                           # attribute of input feild can use other string values as their value
                                           # but must have to include '%s' in that string otherwise by only 
                                           # including the string value it will act like auto_id=True as above.
                                           # '%s' represents the feild name.
                                           
                                           # label_suffix argument is used to change the bydefault ':' after 
                                           # the label of each feild. whatever value provided here will be used.
    
    fm2 = studentRegistration(initial={'name':'RPM','course':'BCA'}) # using initial you can provide initial 
                                                                    # values of form feilds at run-time.

    return render(request,'form/auto_id_eg.html',{'form':fm,'form2':fm2})

