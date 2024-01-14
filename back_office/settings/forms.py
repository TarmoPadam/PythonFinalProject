from django import forms
from .models import Variables


class VariablesForm(forms.ModelForm):
    class Meta:
        model = Variables
        fields = ['website_title']
