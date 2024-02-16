from .models import Music
from django import forms
class MusicForm(forms.Form):
    name = forms.CharField(max_length=20)
    url = forms.URLField()
    cover = forms.CharField(max_length=20)
    category = forms.CharField(max_length=20)