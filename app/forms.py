"""
Definition of forms.
"""
from app.models import Usuario
from django.forms import ModelForm

class Login(ModelForm):
    class Meta:
        model = Usuario
        fields = ['USR_IdRA', 'USR_DssSenha']

