from django.forms import ModelForm

from .models import GerenciaVaga


class GerenteciaVagasForm(ModelForm):

    class Meta:
        model = GerenciaVaga
        fields = '__all__'
