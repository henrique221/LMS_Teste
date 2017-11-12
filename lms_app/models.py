"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Perfil(models.Model):
    PRF_IdPerfil = models.IntegerField(primary_key=True)
    PRF_DssPerfil = models.CharField(max_length=30)

class Usuario(models.Model):
    USR_IdRA = models.IntegerField(primary_key=True)
    USR_DssNome_completo = models.CharField(max_length=70)
    USR_DssSenha = models.CharField(max_length=20)
    USR_IdPerfil = models.ForeignKey(Perfil)



