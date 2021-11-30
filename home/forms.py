from django import forms      
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs = {'placeholder':'name'}),
            "phone_number": forms.TextInput(attrs = {'placeholder':'phone_number'}),
            "email": forms.EmailInput(attrs = {'placeholder':'email'}),
            "message": forms.TextInput(attrs = {'placeholder':'message'})
        }