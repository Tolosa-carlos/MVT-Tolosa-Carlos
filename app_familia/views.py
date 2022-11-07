from django.shortcuts import render
from app_familia.models import Datos_familia

# Create your views here.

def datos_familia(request):
    madre = Datos_familia(nombre = "Astrid Fernandez", edad = 56, nacimiento = "1965/02/17")
    hermana = Datos_familia(nombre = "Ingrid Tolosa", edad = 21, nacimiento = "2001/06/07")
    hermano = Datos_familia(nombre = "Rodrigo Tolosa", edad = 26, nacimiento = "1996/09/16")

    return render(request, "app_familia/vista.html", {"Familia": [madre, hermana, hermano]})
