from django import forms
from .models import student
from django.core import validators # validators will provide some built in validators like 
                                   # MaxLengthValidator,MaxValueValidator,etc.. for the form feilds

def start_with_r(value): # custom validator 
    if  value[0].lower() != 'r':
        raise forms.ValidationError('name should start with r.')

def roll_exist_or_not(value): # custom validator
    data = student.objects.all()
    for stu in data:
        if value == stu.roll:
            raise forms.ValidationError('roll already exist')

class studentDetails(forms.Form):
    name = forms.CharField(validators=[start_with_r,validators.MinLengthValidator(3)])
    roll = forms.IntegerField(validators=[roll_exist_or_not,
        validators.MinValueValidator(100,message='roll should be greater than 100')])