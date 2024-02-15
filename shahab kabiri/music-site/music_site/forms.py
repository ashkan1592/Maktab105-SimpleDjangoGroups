from django import forms
from . models import Musics

class InputForm(forms.ModelForm):
     class Meta:
        model = Musics
        fields = ['name', 'category', 'url', 'cover']
 