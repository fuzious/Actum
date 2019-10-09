
from django import forms
from .models import *
# Create your tests here.
class Productform(forms.ModelForm):
    des = forms.CharField(required=False)
    
    class Meta():
        model=Product
        fields=['des']
class Productform2(forms.ModelForm):
    des = forms.CharField(required=False)
    class Meta():
        model=Product2
        fields=['des']
