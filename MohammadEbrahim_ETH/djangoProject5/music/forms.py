from django import forms
from music.models import Music


class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['name', 'category', 'url', 'cover']
