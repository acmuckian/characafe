from django import forms
from .models import Contact, Newsletter


class ContactForm(forms.ModelForm):
    """
    Form for contact requests
    """
    class Meta:
        model = Contact
        fields = ['name', 'subject', 'email', 'body', ]


class NewsletterForm(forms.ModelForm):
    """
    Form for subscribing to the newsletter
    """
    class Meta:
        model = Newsletter
        fields = ['email', ]
