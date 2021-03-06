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
            name='Vacinas',
            fields=[
                ('id_vacinas', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_vacina', models.TextField(verbose_name='Tipo de Vacina')),
                ('data_vacinacao', models.DateField(verbose_name='Data Vacinação')),
                ('dose', models.TextField(blank=True, verbose_name='Dose da Vacina')),
                ('lote', models.TextField(blank=True, verbose_name='Lote da Vacina')),
                ('local', models.TextField(blank=True, verbose_name='Local da Vacinação')),
                ('fk_usuario_vacinas', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='CadastroDePessoa.usuario')),
            ],
        ),
    ]
