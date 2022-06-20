# Generated by Django 4.0.4 on 2022-06-20 20:34

from django.db import migrations, models
import django_enum_choices.choice_builders
import django_enum_choices.fields
import mainClientes.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=14, unique=True, verbose_name='CPF')),
                ('rg', models.CharField(max_length=10, verbose_name='RG')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('endereco', models.CharField(max_length=80, verbose_name='Endereço')),
                ('telefone', models.CharField(max_length=15, verbose_name='Telefone')),
                ('cidade', models.CharField(max_length=50, verbose_name='Cidade')),
                ('uF', django_enum_choices.fields.EnumChoiceField(choice_builder=django_enum_choices.choice_builders.value_value, choices=[('Acre', 'Acre'), ('Alagoas', 'Alagoas'), ('Amapá', 'Amapá'), ('Amazonas', 'Amazonas'), ('Bahia', 'Bahia'), ('Ceará', 'Ceará'), ('Distrito Federal', 'Distrito Federal'), ('Espírito Santo', 'Espírito Santo'), ('Goiás', 'Goiás'), ('Maranhão', 'Maranhão'), ('Mato Grosso', 'Mato Grosso'), ('Mato Grosso do Sul', 'Mato Grosso do Sul'), ('Minas Gerais', 'Minas Gerais'), ('Pará', 'Pará'), ('Paraíba', 'Paraíba'), ('Paraná', 'Paraná'), ('Pernambuco', 'Pernambuco'), ('Piauí', 'Piauí'), ('Rio Grande do Norte', 'Rio Grande do Norte'), ('Rio Grande do Sul', 'Rio Grande do Sul'), ('Rio de Janeiro', 'Rio de Janeiro'), ('Rondônia', 'Rondônia'), ('Roraima', 'Roraima'), ('Santa Catarina', 'Santa Catarina'), ('São Paulo', 'São Paulo'), ('Sergipe', 'Sergipe'), ('Tocantins', 'Tocantins')], enum_class=mainClientes.models.EnumUF, max_length=19)),
                ('dataHoraCadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data e Hora Cadastro')),
                ('dataHoraAlteracao', models.DateTimeField(auto_now=True, verbose_name='Data e Hora Alteração')),
            ],
        ),
    ]
