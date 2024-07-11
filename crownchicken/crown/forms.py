from django import forms
from .models import ammount

class modelform(forms.ModelForm):
    class Meta:
        model=ammount
        fields='__all__'

