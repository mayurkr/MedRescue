from django import forms
from .models import Patient


class PostForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ('latitude', "longitude")
