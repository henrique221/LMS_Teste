"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from app.models import Usuario, Perfil
from datetime import datetime

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'html/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )



def lista_candidatos(request):
    assert isinstance(request, HttpRequest)

    return render(
        request,
        'html/lista_candidatos.html',
        context_instance = RequestContext(request,
        {
            'title':'Lista de Candidatos',
            'year': datetime.now().year
        })
    )


