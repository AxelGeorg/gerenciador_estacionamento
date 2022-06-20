from enum import Enum
from django.db import models
from django_enum_choices.fields import EnumChoiceField


class EnumUF(Enum):
    AC = "Acre"
    AL = "Alagoas"
    AP = "Amapá"
    AM = "Amazonas"
    BA = "Bahia"
    CE = "Ceará"
    DF = "Distrito Federal"
    ES = "Espírito Santo"
    GO = "Goiás"
    MA = "Maranhão"
    MT = "Mato Grosso"
    MS = "Mato Grosso do Sul"
    MG = "Minas Gerais"
    PA = "Pará"
    PB = "Paraíba"
    PR = "Paraná"
    PE = "Pernambuco"
    PI = "Piauí"
    RN = "Rio Grande do Norte"
    RS = "Rio Grande do Sul"
    RJ = "Rio de Janeiro"
    RO = "Rondônia"
    RR = "Roraima"
    SC = "Santa Catarina"
    SP = "São Paulo"
    SE = "Sergipe"
    TO = "Tocantins"


class Cliente(models.Model):

    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF")
    rg = models.CharField(max_length=10, verbose_name="RG")
    data_nascimento = models.DateField(verbose_name="Data de Nascimento")
    endereco = models.CharField(max_length=80, verbose_name="Endereço")
    telefone = models.CharField(max_length=15, verbose_name="Telefone")
    cidade = models.CharField(max_length=50, verbose_name="Cidade")
    uF = EnumChoiceField(EnumUF)
    dataHoraCadastro = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name="Data e Hora Cadastro")
    dataHoraAlteracao = models.DateTimeField(
        auto_now=True, editable=False, verbose_name="Data e Hora Alteração")

    def __str__(self) -> str:
        return self.nome
