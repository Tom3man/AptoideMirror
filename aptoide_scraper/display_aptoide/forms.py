# listings/forms.py

from django import forms

class ContactUsForm(forms.Form):
   url = forms.CharField(required=True)
   email = forms.EmailField()
   message = forms.CharField(max_length=1000)