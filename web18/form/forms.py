from django import forms

class studentRegistration(forms.Form):
    name = forms.CharField()
    mobile = forms.IntegerField()
    email = forms.EmailField()
    course = forms.CharField()

    key = forms.CharField(widget=forms.HiddenInput()) 
    
    
    