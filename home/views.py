from django.shortcuts import render
from home.models import Pintura

def home(request):
    return render(request, 'home/home.html')

def listado_de_pinturas(request):
    
    pinturas = Pintura.objects.all()
    
    return render(request, 'home/pinturas.html', {'pinturas': pinturas})