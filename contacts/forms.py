from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['message']
        widgets = {
            'message' : forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your message here',
                'rows': 5
            })
        }
    