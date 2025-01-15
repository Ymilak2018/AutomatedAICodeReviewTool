from django import forms
from .models import Message
class CBform(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
