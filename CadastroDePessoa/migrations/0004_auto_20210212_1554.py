# Generated by Django 3.1.5 on 2021-02-12 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CadastroDePessoa', '0003_auto_20210212_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='qrcode',
            field=models.TextField(blank=True, verbose_name='QRCode'),
        ),
    ]
