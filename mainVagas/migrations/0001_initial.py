# Generated by Django 4.0.4 on 2022-06-21 12:41

from django.db import migrations, models
import django_enum_choices.choice_builders
import django_enum_choices.fields
import mainVagas.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', django_enum_choices.fields.EnumChoiceField(choice_builder=django_enum_choices.choice_builders.value_value, choices=[('Disponível', 'Disponível'), ('Ocupado', 'Ocupado')], default=mainVagas.models.EnumStatus['disponivel'], enum_class=mainVagas.models.EnumStatus, max_length=10)),
                ('setor', models.CharField(max_length=2)),
                ('tipoVeiculo', django_enum_choices.fields.EnumChoiceField(choice_builder=django_enum_choices.choice_builders.value_value, choices=[('Pequeno', 'Pequeno'), ('Médio', 'Médio'), ('Grande', 'Grande')], enum_class=mainVagas.models.EnumTipoVeiculo, max_length=7)),
                ('dataHoraCadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data e Hora Cadastro')),
                ('dataHoraAlteracao', models.DateTimeField(auto_now=True, verbose_name='Data e Hora Alteração')),
            ],
        ),
    ]
