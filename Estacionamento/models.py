from enum import Enum
from django.db import models
from django_enum_choices.fields import EnumChoiceField

from mainCarros.models import Carro
from mainVagas.models import Vaga


class GerenciaVaga(models.Model):

    vaga = models.ForeignKey(
        Vaga, unique=True, on_delete=models.CASCADE, editable=False)
    carro = models.ForeignKey(Carro, unique=True, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self) -> str:
        return self.vaga.setor + " - " + self.carro.placa
