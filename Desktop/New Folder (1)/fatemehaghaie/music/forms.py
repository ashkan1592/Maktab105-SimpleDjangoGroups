from django import forms
from .models import Music
class Music_Form(forms.ModelForm):
    class Meta:
        model = Music
        fields=["name", "category", "url","cover"]

