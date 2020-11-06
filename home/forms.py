from django import forms
class NewProjForm(forms.Form):
    creator_handle = forms.CharField(max_length=17)

