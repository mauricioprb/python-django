from django import forms
from django.db import models

class BuscaUsuarioForm(forms.Form):    
    #1 campo da tupla fica no banco de dados
    #2 campo da tupla eh mostrado para o usuario
    TIPOS_USUARIOS = (
        (None, '-----'),
        ('ADMINISTRADOR', 'Administrador'),
        ('ENFERMEIRO', 'Enfermeiro' ),
        ('MÉDICO', 'Médico' ),
        ('TÉCNICO', 'Técnico' ),
    )
    nome = forms.Field(label='Nome do Usuário *', required=False)
    tipo = forms.ChoiceField(label='Tipo de Usuário', choices=TIPOS_USUARIOS, required=False)
    