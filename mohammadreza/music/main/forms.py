from django.forms import ModelForm
from .models import Add,Category
from django import forms



class CategoryForm(forms.Form):
    name=forms.CharField(max_length=200)

    def save(self):
        category_save=Category()
        category_save.name=self.cleaned_data['name']
        category_save.save()



class Form(ModelForm):
    class Meta:
        model=Add
        exclude=('is_delete',)