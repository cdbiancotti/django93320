from django import forms
from home.models import Pintura


class PinturaForm(forms.ModelForm):
    class Meta:
        model = Pintura
        fields = ("nombre", "autor", "descripcion")
