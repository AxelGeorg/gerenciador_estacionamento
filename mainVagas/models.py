from enum import Enum
from django.db import models
from django_enum_choices.fields import EnumChoiceField


class EnumTipoVeiculo(Enum):
    pequeno = "Pequeno"
    medio = "Médio"
    grande = "Grande"


class EnumStatus(Enum):
    disponivel = "Disponível"
    ocupado = "Ocupado"


class Vaga(models.Model):
    status = EnumChoiceField(EnumStatus, default=EnumStatus.disponivel)
    setor = models.CharField(max_length=2)
    tipoVeiculo = EnumChoiceField(EnumTipoVeiculo)
    dataHoraCadastro = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name="Data e Hora Cadastro")
    dataHoraAlteracao = models.DateTimeField(
        auto_now=True, editable=False, verbose_name="Data e Hora Alteração")

    def __str__(self) -> str:
        return "Vaga " + self.setor + " - " + self.tipoVeiculo.value
