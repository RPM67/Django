from django import forms
from django.core.validators import RegexValidator
class courseRegistration(forms.Form):
    Name_validator = RegexValidator(
        regex=r'^[a-zA-Z]*$',
        message='Enter a valid course name',
    )
    Name = forms.CharField(min_length=2,label='Course Name', widget=forms.TextInput(attrs={'class': 'form-control'}),validators=[Name_validator], error_messages={'required': 'Enter course name here','min_length':'Enter a valid course name'})
    Id = forms.IntegerField(label='Course Id', widget=forms.TextInput(attrs={'class': 'form-control'}), error_messages={'required': 'Enter course id here','invalid':'Enter a valid course Id(must be a number)'})
    DURATION_CHOICES = [
        ('', 'Select duration'),
        ('1 month', '1 Month'),
        ('3 months', '3 Months'),
        ('6 months', '6 Months'),
        ('1 year', '1 Year'),
        ('2 year', '2 Year'),
        ('3 year', '3 Year'),
        ('4 year', '4 Year'),
        ('5 year', '5 Year'),
    ]
    Duration = forms.ChoiceField(choices=DURATION_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}), error_messages={'required': 'select a course duration here'})
    Seats = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}), error_messages={'required': 'Enter total available course seats here','invalid':'Enter a valid number for seats'})
    Fees = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}), error_messages={'required': 'Enter total course fees here','invalid':'Enter a valid number for fees'})
