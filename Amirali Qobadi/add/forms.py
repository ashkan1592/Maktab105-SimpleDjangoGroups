from django import forms


class AddForm(forms.Form):
    name = forms.CharField()
    cover = forms.CharField()
    category = forms.CharField()
    url = forms.CharField()
