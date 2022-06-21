# Generated by Django 4.0.4 on 2022-06-21 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainCarros', '0001_initial'),
        ('mainVagas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GerenciaVaga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.CharField(max_length=100)),
                ('carro', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainCarros.carro')),
                ('vaga', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='mainVagas.vaga')),
            ],
        ),
    ]
