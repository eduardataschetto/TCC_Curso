# Generated by Django 3.1.5 on 2021-02-13 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Historico', '0004_auto_20210212_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicofamiliar',
            name='doenca_cronica',
            field=models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3, verbose_name='Doença Crônica'),
        ),
    ]
