from django import forms
from .models import Event

class EntryForm (forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'eventdate', 'rating', 'image']

class LoginForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())
