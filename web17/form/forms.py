from django import forms

class studentRegistration(forms.Form):
    mobile = forms.IntegerField()
    email = forms.EmailField()
    course = forms.CharField(initial='BCA') # you can either provide initial value for feilds either here or in
                                            #  views.py file. 
    name = forms.CharField()
    
    