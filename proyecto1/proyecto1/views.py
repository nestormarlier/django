from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

class Persona (object):
    
    def __init__(self,nombre,apellido):
        
        self.nombre=nombre
        self.apellido=apellido

def saludo(request):
   
    p1=Persona("Néstor Oscar","Marlier")
    
    # nombre="Néstor"
    # apellido="Marlier"
    
    ahora=datetime.datetime.now()
    
    #doc_externo=open("C:\plantillas\miplantilla.html")
    
    #plt=Template(doc_externo.read())
    
    #doc_externo.close()
    
    #doc_externo=get_template('miplantilla.html')
    
    #ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"fecha_actual":ahora,"temas":["Plantillas","Modelos","Formularios","Vistas","Despliegue"]})
    
    #documento=doc_externo.render({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"fecha_actual":ahora,"temas":["Plantillas","Modelos","Formularios","Vistas","Despliegue"]})

    #return HttpResponse(documento)
    
    return render(request,"miplantilla.html",{"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"fecha_actual":ahora,"temas":["Plantillas","Modelos","Formularios","Vistas","Despliegue"]})

def despedida(request):
    return HttpResponse("Hasta luego alumnos de Django")

def cursoC(request):
    
    fecha_actual=datetime.datetime.now()
    
    return render(request,"cursoC.html",{"dameFecha":fecha_actual})
def cursoCss(request):
    
    fecha_actual=datetime.datetime.now()
    
    return render(request,"cursoCss.html",{"dameFecha":fecha_actual})


def dameFecha(request):
    
    fecha_actual=datetime.datetime.now()
    
    documento="""<html>
    <body>
    <h2>
    Fecha y hora actuales %s
    </h2>
    </body>
    </html>""" % fecha_actual
    
    return HttpResponse(documento)

def calculaEdad(request,edad,anio):
    #edadActual=18
    periodo=anio-2019
    edadFutura=edad+periodo
    documento="<html><body><h2>En el año %s tendras %s años" %(anio,edadFutura)
    
    return HttpResponse(documento)