from django import forms

class differentFormFeilds(forms.Form):
    name = forms.CharField(required=False)
    roll = forms.IntegerField(required=False)
    height1 = forms.DecimalField(required=False)
    height2 = forms.FloatField(required=False)
    url = forms.URLField(required=False)
    date = forms.DateField(required=False)
    time = forms.TimeField(required=False)
    dateTime = forms.DateTimeField(required=False)
    duration = forms.DurationField(required=False)
    file = forms.FileField(allow_empty_file=True, required=False)
    filepath = forms.FilePathField( path='C:/', required=False)
    image = forms.ImageField(required=False)
    CHOICES = [('','select'),
               ('01','BCA'),
               ('02','BBA'),
               ('03','MBA'),
               ('04','MCA'),
               ]
    choice = forms.ChoiceField(choices=CHOICES, required=False)
    multiChoice = forms.MultipleChoiceField( choices=CHOICES, required=False)
    ip = forms.GenericIPAddressField(required=False)
    nullBoolean = forms.NullBooleanField(required=False)
    textarea = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':50}),required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    agree = forms.BooleanField(label='I agree ', label_suffix=' ')
    