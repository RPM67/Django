from django import forms
from .models import data

class courseReg(forms.Form):
    id = forms.IntegerField(label='Course Id ')
    name = forms.CharField( max_length=40, label='Course Name ')
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        cor_data = data.objects.all()
        
        
        valId = self.cleaned_data ['id']
        valName = self.cleaned_data['name']
        valPass = self.cleaned_data['password']
        
        for cor in cor_data:
            
            if cor.course_id == valId:
                raise forms.ValidationError('course id already exist.')
            
            if cor.course_name == valName:
                raise forms.ValidationError('cannot have multiple courses with same name.')
            
        if len(valPass) < 8:
                raise forms.ValidationError('password should not be less than 8 digits.')