from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from django.template import loader  

def vista_familia(request):

    datos = {"nombre": "Carlos", "fecha": datetime.now(), "apellido": "Tolosa"}

    plantilla = loader.get_template("familia.html")

    documento = plantilla.render(datos)

    return HttpResponse(documento)