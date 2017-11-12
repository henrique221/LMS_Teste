"""
Definition of forms.
"""

from django import forms
from lms_app.models import *
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class Login(forms.ModelForm):
    class Meta:
        model = Usuario
        widgets = {
            'USR_DssSenha' : forms.PasswordInput(),
        }