from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    
    class Meta:
        models = Contact
        fields = [
            'subject',
            'message',
            'email',
        ]