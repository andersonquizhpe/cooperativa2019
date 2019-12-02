from django.shortcuts import render

# Create your views here.
def principal_pagina(request):
    context={
        'title': 'COOPERATIVA QUINTO',
    }
    return render (request, 'principal.html', context)