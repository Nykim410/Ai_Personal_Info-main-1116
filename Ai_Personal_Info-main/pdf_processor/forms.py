from django import forms
from .models import PolicyDocument

class PolicyDocumentForm(forms.ModelForm):
    class Meta:
        model = PolicyDocument
        fields = ['file'] 
