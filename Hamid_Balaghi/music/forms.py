from django import forms
from .models import Song


# class AddForm(forms.Form):
#     name = forms.CharField()
#     cover = forms.CharField()
#     url = forms.CharField()
#     category = forms.CharField()


##
class AddSongForm(forms.ModelForm):
    category_name = forms.CharField(max_length=100)

    class Meta:
        model = Song
        fields = ['name', 'cover', 'url']

    # def clean_category_name(self):
    #     category_name = self.cleaned_data['category_name']
    #     if not category_name:
    #         raise forms.ValidationError("Category name is required.")
    #     return category_name


