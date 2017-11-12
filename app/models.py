"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Perfil(models.Model):
    PRF_IdPerfil = models.IntegerField(primary_key=True)
    PRF_DssPerfil = models.CharField(max_length=15)



class Usuario(models.Model):
    USR_IdRA = models.IntegerField(primary_key=True)
    USR_DssNome = models.CharField(max_length=70)
    USR_DssSenha = models.CharField(max_length=12)
    USR_IdPerfil = models.ForeignKey(Perfil)



