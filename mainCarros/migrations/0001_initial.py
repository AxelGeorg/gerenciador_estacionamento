# Generated by Django 4.0.4 on 2022-06-21 12:41

from django.db import migrations, models
import django.db.models.deletion
import django_enum_choices.choice_builders
import django_enum_choices.fields
import mainCarros.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainClientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=20)),
                ('marca', django_enum_choices.fields.EnumChoiceField(choice_builder=django_enum_choices.choice_builders.value_value, choices=[('AGRALE', 'AGRALE'), ('ALFA ROMEO', 'ALFA ROMEO'), ('AM GENERAL', 'AM GENERAL'), ('ASIA MOTORS', 'ASIA MOTORS'), ('ASTON MARTIN', 'ASTON MARTIN'), ('AUDI', 'AUDI'), ('BENTLEY', 'BENTLEY'), ('BMW', 'BMW'), ('BYD', 'BYD'), ('CAOA CHERY', 'CAOA CHERY'), ('CHANA', 'CHANA'), ('CHANGAN', 'CHANGAN'), ('CHERY', 'CHERY'), ('CHEVROLET', 'CHEVROLET'), ('CHRYSLER', 'CHRYSLER'), ('CITROEN', 'CITROEN'), ('DAEWOO', 'DAEWOO'), ('DAIHATSU', 'DAIHATSU'), ('DODGE', 'DODGE'), ('DS', 'DS'), ('EFFA', 'EFFA'), ('FERRARI', 'FERRARI'), ('FIAT', 'FIAT'), ('FORD', 'FORD'), ('FOTON', 'FOTON'), ('GEELY', 'GEELY'), ('HONDA', 'HONDA'), ('HYUNDAI', 'HYUNDAI'), ('IVECO', 'IVECO'), ('JAC', 'JAC'), ('JAGUAR', 'JAGUAR'), ('JEEP', 'JEEP'), ('JINBEI', 'JINBEI'), ('KIA', 'KIA'), ('LAMBORGHINI', 'LAMBORGHINI'), ('LAND ROVER', 'LAND ROVER'), ('LEXUS', 'LEXUS'), ('LIFAN', 'LIFAN'), ('MAHINDRA BRAMONT', 'MAHINDRA BRAMONT'), ('MASERATI', 'MASERATI'), ('MAZDA', 'MAZDA'), ('MCLAREN', 'MCLAREN'), ('MERCEDES BENZ', 'MERCEDES BENZ'), ('MINI', 'MINI'), ('MITSUBISHI', 'MITSUBISHI'), ('MORRIS GARAGES', 'MORRIS GARAGES'), ('NISSAN', 'NISSAN'), ('PEUGEOT', 'PEUGEOT'), ('PORSCHE', 'PORSCHE'), ('RAM', 'RAM'), ('RELY', 'RELY'), ('RENAULT', 'RENAULT'), ('ROLLS ROYCE', 'ROLLS ROYCE'), ('SEAT', 'SEAT'), ('SHINERAY', 'SHINERAY'), ('SMART', 'SMART'), ('SSANGYONG', 'SSANGYONG'), ('SUBARU', 'SUBARU'), ('SUZUKI', 'SUZUKI'), ('TAC', 'TAC'), ('TOYOTA', 'TOYOTA'), ('TROLLER', 'TROLLER'), ('VOLKSWAGEN', 'VOLKSWAGEN'), ('VOLVO', 'VOLVO')], enum_class=mainCarros.models.EnumMarcas, max_length=16)),
                ('cor', models.CharField(max_length=20)),
                ('ano', models.IntegerField()),
                ('placa', models.CharField(max_length=15, unique=True)),
                ('dataHoraCadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data e Hora Cadastro')),
                ('dataHoraAlteracao', models.DateTimeField(auto_now=True, verbose_name='Data e Hora Alteração')),
                ('ocupandoVaga', models.BooleanField(default=False, editable=False)),
                ('proprietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainClientes.cliente')),
            ],
        ),
    ]
