from enum import Enum
from django.db import models
from django_enum_choices.fields import EnumChoiceField

from mainClientes.models import Cliente

# Create your models here.


class EnumMarcas(Enum):
    AGRALE = "AGRALE"
    ALFA_ROMEO = "ALFA ROMEO"
    AM_GENERAL = "AM GENERAL"
    ASIA_MOTORS = "ASIA MOTORS"
    ASTON_MARTIN = "ASTON MARTIN"
    AUDI = "AUDI"
    BENTLEY = "BENTLEY"
    BMW = "BMW"
    BYD = "BYD"
    CAOA_CHERY = "CAOA CHERY"
    CHANA = "CHANA"
    CHANGAN = "CHANGAN"
    CHERY = "CHERY"
    CHEVROLET = "CHEVROLET"
    CHRYSLER = "CHRYSLER"
    CITROEN = "CITROEN"
    DAEWOO = "DAEWOO"
    DAIHATSU = "DAIHATSU"
    DODGE = "DODGE"
    DS = "DS"
    EFFA = "EFFA"
    FERRARI = "FERRARI"
    FIAT = "FIAT"
    FORD = "FORD"
    FOTON = "FOTON"
    GEELY = "GEELY"
    HONDA = "HONDA"
    HYUNDAI = "HYUNDAI"
    IVECO = "IVECO"
    JAC = "JAC"
    JAGUAR = "JAGUAR"
    JEEP = "JEEP"
    JINBEI = "JINBEI"
    KIA = "KIA"
    LAMBORGHINI = "LAMBORGHINI"
    LAND_ROVER = "LAND ROVER"
    LEXUS = "LEXUS"
    LIFAN = "LIFAN"
    MAHINDRA_BRAMONT = "MAHINDRA BRAMONT"
    MASERATI = "MASERATI"
    MAZDA = "MAZDA"
    MCLAREN = "MCLAREN"
    MERCEDES_BENZ = "MERCEDES BENZ"
    MINI = "MINI"
    MITSUBISHI = "MITSUBISHI"
    MORRIS_GARAGES = "MORRIS GARAGES"
    NISSAN = "NISSAN"
    PEUGEOT = "PEUGEOT"
    PORSCHE = "PORSCHE"
    RAM = "RAM"
    RELY = "RELY"
    RENAULT = "RENAULT"
    ROLLS_ROYCE = "ROLLS ROYCE"
    SEAT = "SEAT"
    SHINERAY = "SHINERAY"
    SMART = "SMART"
    SSANGYONG = "SSANGYONG"
    SUBARU = "SUBARU"
    SUZUKI = "SUZUKI"
    TAC = "TAC"
    TOYOTA = "TOYOTA"
    TROLLER = "TROLLER"
    VOLKSWAGEN = "VOLKSWAGEN"
    VOLVO = "VOLVO"


class Carro(models.Model):

    modelo = models.CharField(max_length=20)
    marca = EnumChoiceField(EnumMarcas)
    cor = models.CharField(max_length=20)
    ano = models.IntegerField()
    placa = models.CharField(max_length=15, unique=True)
    proprietario = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    dataHoraCadastro = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name="Data e Hora Cadastro")
    dataHoraAlteracao = models.DateTimeField(
        auto_now=True, editable=False, verbose_name="Data e Hora Alteração")

    def __str__(self) -> str:
        return self.modelo + " - " + self.placa
