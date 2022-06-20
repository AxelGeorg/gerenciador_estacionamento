from django.forms import ModelForm

from .models import GerenciaVaga


class GerenteciaVagasForm(ModelForm):

    class Meta:
        model = GerenciaVaga
        fields = '__all__'

    def save(self):
        obj = super().save(commit=False)
        obj.save()
        return obj
