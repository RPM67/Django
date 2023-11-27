from django import forms

class passwordCheck(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     pw = cleaned_data['password']
    #     cnfrm_pw = cleaned_data['confirm_password']
        
    #     if pw != cnfrm_pw:
    #         raise forms.ValidationError('Password did not matched.')