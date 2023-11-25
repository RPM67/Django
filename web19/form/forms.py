from django import forms

class studentRegistration(forms.Form):
    name = forms.CharField(label='Your Name', label_suffix=' - ', initial='RPM',
                            required=False, help_text='Limit 70 char')
    
    
    # widget example
    feedback = forms.CharField(widget=forms.Textarea)
    file = forms.CharField(widget=forms.TextInput(attrs={'class':'some1 some2', # attrs will add class 'some1',
                          'id':'hello'}))                                       # 'some2' in the input feild here. 
                                                                               # later this class can be used for 
                                                                              # css of input feild. 'id' will 
                                                                             # change id and for value of input,
                                                                            # label feild.