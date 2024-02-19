from django import forms
from .models import Music, Category


class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ["name", "url", "categories", "cover"]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
