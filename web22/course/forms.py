from django import forms
from .models import data

class courseReg(forms.Form):
    id = forms.IntegerField(label='Course Id ')
    name = forms.CharField( max_length=40, label='Course Name ')
    
    def clean_id(self):
        cor_data = data.objects.all()
        val = self.cleaned_data['id']
        for cor in cor_data:
            if cor.course_id == val:
                raise forms.ValidationError('course id alreay exist')
        return val