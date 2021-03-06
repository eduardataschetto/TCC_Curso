# Generated by Django 3.1.5 on 2021-02-04 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CadastroDePessoa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banco_Medicamento_Anvisa',
            fields=[
                ('id_anvisa', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(verbose_name='Nome Medicamento')),
            ],
        ),
        migrations.CreateModel(
            name='Medicamentos',
            fields=[
                ('id_medicamentos', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(default='', max_length=100, verbose_name='Nome')),
                ('funcao', models.TextField(blank=True, verbose_name='Função')),
                ('data_inicio', models.DateField(blank=True, verbose_name='Data de Início')),
                ('data_final', models.DateField(blank=True, verbose_name='Data Final')),
                ('infos_extras', models.TextField(blank=True, verbose_name='Informações Extras')),
                ('fk_user_medicacao', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='CadastroDePessoa.usuario')),
            ],
        ),
    ]
