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
            name='HistoricoFamiliar',
            fields=[
                ('id_historico_familiar', models.AutoField(primary_key=True, serialize=False)),
                ('doenca_hereditarias', models.TextField(blank=True, verbose_name='Doenças Hereditarias')),
                ('tipo_doenca', models.TextField(blank=True, verbose_name='Tipo da Doença')),
                ('grau_parentesco', models.CharField(choices=[('primeiro_grau', 'Primeiro Grau'), ('segundo_grau', 'Segundo Grau'), ('Terceiro_grau', 'Terceiro Grau'), ('outros', 'Outros')], max_length=13, verbose_name='Grau Parentesco')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricoConsultas',
            fields=[
                ('id_historico_consultas', models.AutoField(primary_key=True, serialize=False)),
                ('lugar', models.TextField(verbose_name='Lugar')),
                ('data', models.DateField(verbose_name='Data Consulta')),
                ('receita', models.FileField(blank=True, upload_to='', verbose_name='Receita')),
                ('atestado', models.FileField(blank=True, upload_to='', verbose_name='Atestado')),
                ('fk_usuario_historico_consulta', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='CadastroDePessoa.usuario')),
            ],
        ),
    ]
