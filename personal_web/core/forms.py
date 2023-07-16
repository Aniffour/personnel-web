from django import forms

class ContactFORM(forms.Form):
    username = forms.CharField(max_length=100 , required=True)
    subject=forms.CharField(widget=forms.Textarea(attrs={ 'placeholder': 'Enter your message', 'required': True}))
    email = forms.EmailField()
