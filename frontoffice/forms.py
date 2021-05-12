from django import forms
from django.db.models import fields
from .models import Maison,Appartement
class LogementForm(forms.ModelForm):
    class Meta:
        model=[Maison,Appartement]
        fields ="__all__"