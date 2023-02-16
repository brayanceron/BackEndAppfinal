from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.views.generic import View
from .consultasMogoDB import getMisTutoriasMongo,getTutoriaMongo,registrarTutoriaMongo,getContenidoTutoriaMongo,getEntradaMongo,registrarEntradaMongo,updateEntradaMongo
import json




def root(request):
    return HttpResponse("Oki")

@csrf_exempt 
def rutaUno(request):
    
    if request.method == 'GET':
        print("Peticion get recivida")
        return JsonResponse({"prueba_get":"OK","atributo2":"valor 2"})
    
    elif request.method == 'POST':
        print("Peticion post recivida")
        data =json.loads(request.body.decode("utf-8")) 
        print(data)
        print(data["datos_peticion"])
        return JsonResponse({"prueba_post":"OK"})
    

@csrf_exempt 
def getmisTutorias(request):
    datarecivida =json.loads(request.body.decode("utf-8")) 
        
    id_usuario=datarecivida['id_usuario']
    
    print("Enviando  tutorias del usuario: "+id_usuario )
    listaR=json.loads(getMisTutoriasMongo(id_usuario)) #se convierte a json la cadena que viene en formato json
    return JsonResponse((listaR),safe=False)
    
    
@csrf_exempt 
def getTutoria(request):
    if request.method == 'POST':
        print("Buscando tutoria")
        datarecivida =json.loads(request.body.decode("utf-8")) 
        
        id_tutoria=datarecivida['id_tutoria']
        listaR=json.loads(getTutoriaMongo(id_tutoria))
        return JsonResponse((listaR),safe=False)
    
@csrf_exempt 
def getContenidoTutoria(request):
    if request.method == 'POST':
        print("Buscando Contenido de la tutoria")
        datarecivida =json.loads(request.body.decode("utf-8")) 
        
        id_tutoria=datarecivida['id_tutoria']
        listaR=json.loads(getContenidoTutoriaMongo(id_tutoria))
        print(listaR)
        return JsonResponse((listaR),safe=False)
        
        #return JsonResponse({"ok":"ok"},safe=False)

@csrf_exempt 
def registrarTutoria(request):
    if request.method == 'POST':
        print("registrando tutoria")
        datarecivida =json.loads(request.body.decode("utf-8")) 
        
        nombre=datarecivida['nombre']
        id_profesor=datarecivida['id_profesor']
        descripcion=datarecivida['descripcion']
        
        jsondata={
            "nombre":nombre,
            "id_profesor":{"$oid":id_profesor},
            "id_estudiantes":[],
            "estado":"Activo",
            "descripcion":descripcion,
            "calificacion":0,
            "tipo":"I",
            "entradas":[]
        }
        dd=[nombre,id_profesor,descripcion]
        
        print("----------------------------------")
        print(jsondata)
        print(type(jsondata))
        print("----------------------------------")
        registrarTutoriaMongo(dd)
        
        #listaR=json.loads(getTutoriaMongo(id_tutoria))
        return JsonResponse({"ok":"ok"},safe=False)


@csrf_exempt 
def getEntrada(request):
    if request.method == 'POST':
        print("Buscando entrada de la tutoria")
        datarecivida =json.loads(request.body.decode("utf-8")) 
        
        id_entrada=datarecivida['id_entrada']
        print(id_entrada)
        listaR=json.loads(getEntradaMongo(id_entrada))
        print(listaR)
        return JsonResponse((listaR),safe=False)
    
    
@csrf_exempt 
def registrarEntrada(request):
    if request.method == 'POST':
        print("registrando entrada")
        datarecivida =json.loads(request.body.decode("utf-8")) 
        
        titulo=datarecivida['titulo']
        id_tutoria=datarecivida['id_tutoria']        
        id_profesor=datarecivida['id_profesor']
        descripcion=datarecivida['descripcion']
        
        data=[id_tutoria,id_profesor,titulo,descripcion]

        registrarEntradaMongo(data)
        
        #listaR=json.loads(getTutoriaMongo(id_tutoria))
        return JsonResponse({"ok":"ok"},safe=False)

@csrf_exempt 
def updateEntrada(request):
    if request.method == 'POST':
        print("registrando entrada")
        datarecivida =json.loads(request.body.decode("utf-8")) 
        print("--------------------------------------")
        print("datarecivida: "+str(datarecivida))
        
        titulo=datarecivida['titulo']
        descripcion=datarecivida['descripcion']
        id_entrada=datarecivida['id_entrada']     
        
        
        data=[id_entrada,titulo,descripcion]

        updateEntradaMongo(data)
        
        #listaR=json.loads(getTutoriaMongo(id_tutoria))
        return JsonResponse({"ok":"ok"},safe=False)
    
    
    
    
    
    
    