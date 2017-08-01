from django import forms

from .validators import validate_url, validate_dot_com

'''
    Different methods to perform validations:
    1. Pass validators list as kwargs to field.
    2. Perform all the validation in clean method.
    3. Perform indivsual validation in clean_<fieldname> method.
'''


class SubmitUrlForm(forms.Form):
    url = forms.CharField(
        label='Submit URL', 
        validators=[validate_url, validate_dot_com],
        widget=forms.TextInput(
                attrs={
                    "placeholder": "Long URL",
                    "class": "form-control"
                }
            )
        )

    # Cleans all the fields of the forms
    # Calls indivisual clean methods
    # Calling the super constructor is necessary.
    # def clean(self):
    #     cleaned_data = super(SubmitUrlForm, self).clean()
       
    # # Name of method is Clean_<fieldname>
    # def clean_url(self):
    #     url = self.cleaned_data.get("url")
    #     url_validator = URLValidator()
    #     try:
    #         url_validator(url)
    #     except:
    #         raise forms.ValidationError("Invalid URL")    
    #     return url