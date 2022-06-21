from django import forms
from django.forms import ModelForm

from mainCarros.models import Carro

from .models import GerenciaVaga


class GerenteciaVagasForm(forms.ModelForm):

    carro = forms.ModelChoiceField(
        queryset=Carro.objects.filter(ocupandoVaga=False)
    )

    class Meta:
        model = GerenciaVaga
        fields = ('carro', 'valor',)

    def save(self):
        obj = super().save(commit=False)
        obj.save()
        return obj
