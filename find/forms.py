from django import forms
from .models import Lost

class NewLost(forms.ModelForm):  
    photo = forms.ImageField()       
    class Meta:
        model = Lost
        fields=['title','photo','body',] 