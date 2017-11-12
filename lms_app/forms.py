"""
Definition of forms.
"""

from django import forms
from lms_app.models import *

class Login(forms.ModelForm):
    class Meta:
        model = Usuario
        widgets = {
            'USR_DssSenha' : forms.PasswordInput(),
        }