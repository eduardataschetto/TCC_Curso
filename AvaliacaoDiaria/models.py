from django.db import models
from multiselectfield import MultiSelectField
from CadastroDePessoa.models import Usuario

from django.utils import timezone


class AvaliacaoDiaria(models.Model):
    SINTOMAS_CHOICES = (
        ('dorDeCabeca', 'Dor de Cabeça'),
        ('dorNoCorpo', 'Dor no corpo'),
        ('cansaco', 'Cansaço'),
        ('dorNoEstomago', 'Dor no estômago'),
        ('inchaco', 'Inchaço'),
        ('nausea', 'Náusea'),
        ('coriza', 'Coriza'),
        ('faltaDeAr', 'Falta de ar'),
        ('insonia', 'Insonia'),
        # ('outro', 'Outro'),
    )
    id_avaliacao_diaria = models.AutoField(primary_key=True) 
    sintomas = MultiSelectField('Sintomas', choices=SINTOMAS_CHOICES, max_length=50, max_choices=10)
    observacoes = models.TextField('Observações', blank=True)
    outro = models.TextField('Outro sintoma', blank=True)
    data = models.DateField('Data ', default=timezone.now())
    fk_usuario_avaliacao_diaria = models.ForeignKey(Usuario, on_delete=models.CASCADE, default="")

