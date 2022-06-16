"""
All forms used for XML conversion
"""
from django import forms
 
class XMLConverterForm(forms.Form):
    file = forms.FileField(
        label="XML File",
        error_messages={'required': 'An XML file is required'}
    )