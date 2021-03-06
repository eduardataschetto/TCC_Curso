from django import forms
from django.forms import ModelForm
from .models import Usuario


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'nascimento', 'sexo', 'email', 'telefone']


class UsuarioUpdateForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'nascimento', 'sexo', 'email', 'telefone', 'foto']
