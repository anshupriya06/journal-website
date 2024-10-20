from django import forms
from .models import JASER

class JASERForm(forms.ModelForm):
    class Meta:
        model = JASER
        fields = ['name', 'description', 'pdf_file']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'pdf_file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

