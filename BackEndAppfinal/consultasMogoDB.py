from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps
from datetime import datetime


client = MongoClient()
client = MongoClient('localhost', 27017)

db = client.BDAPPFINAL
collection = db.tutorias





def getMisTutoriasMongo(id_usuario):
    pipeline = [
    {"$match":{"id_estudiantes":ObjectId(id_usuario)}},
    {"$lookup": {"from":"profesores","localField":"id_profesor","foreignField":"_id","as":"id_profesor"}},
    ]
    results=collection.aggregate(pipeline)
    list_cur = list(results)#convirtiendo a diccionario el resultado
    json_string_data = dumps(list_cur)#convirtiendo a json el diccionario anterior
    return json_string_data #se devuelve una cadena en formato json

def getTutoriaMongo(id_tutoria):
    
    pipeline = [
    {"$match": {"_id": ObjectId(id_tutoria)}},
    {"$lookup": {"from":"profesores","localField":"id_profesor","foreignField":"_id","as":"id_profesor"}},
    {"$lookup": {"from":"estudiantes","localField":"id_estudiantes","foreignField":"_id","as":"id_estudiantes"}},
    ]
    
    results=collection.aggregate(pipeline)
    list_cur = list(results)
    

    
    json_string_data = dumps(list_cur)#convirtiendo a json el diccionario anterior
    return json_string_data #se devuelve una cadena en formato json


def registrarTutoriaMongo(json_data):
    print(json_data)
    print(type(json_data))

    
    save={
            "nombre":json_data[0],
            "id_profesor":ObjectId(json_data[1]),
            "id_estudiantes":[],
            "estado":"Activo",
            "descripcion":json_data[2],
            "calificacion":0,
            "tipo":"I",
            "entradas":[]
        }
    print(save)
    
    
    
    results=collection.insert_one(save);



def getContenidoTutoriaMongo(id_tutoria):
    pipeline = [
    {"$match": {"_id": ObjectId(id_tutoria)}},
    {"$lookup": {"from":"entradasTutorias","localField":"entradas","foreignField":"_id","as":"entradas"}},
    {"$lookup": {"from":"profesores","localField":"id_profesor","foreignField":"_id","as":"id_profesor"}},
    ]
    
    results=collection.aggregate(pipeline)
    list_cur = list(results)
    

    
    json_string_data = dumps(list_cur)#convirtiendo a json el diccionario anterior
    return json_string_data #se devuelve una cadena en formato json

def getEntradaMongo(id_tutoria):
    pipeline = [
    {"$match": {"_id": ObjectId(id_tutoria)}},
    {"$lookup": {"from":"profesores","localField":"id_profesor","foreignField":"_id","as":"id_profesor"}},
    ]
    
    results=db.entradasTutorias.aggregate(pipeline)
    list_cur = list(results)
    
    json_string_data = dumps(list_cur)#convirtiendo a json el diccionario anterior
    return json_string_data #se devuelve una cadena en formato json
#


def registrarEntradaMongo(data):
    print(data)
    print(type(data))
    now = datetime.now()
    fecha_creacion= str(now.day)+"/"+str(now.month)+"/"+str(now.year)+"   "+str(now.hour)+":"+str(now.minute)
    
    save={            
            "id_tutoria":ObjectId(data[0]),
            "id_profesor":ObjectId(data[1]),
            "titulo":data[2],
            "descripcion":data[3],
            "fecha_creacion":fecha_creacion,
            "archivos":[],
        }
    print(save)
    
    #results=db.entradasTutorias.insert_one(save)
    insesrcion=db.entradasTutorias.insert_one(save)
    
    
    id_insesrcion=insesrcion.inserted_id
    #print ("id insertado: "+str(id_insesrcion))
    collection.update_one(
    {"_id": ObjectId(data[0])   },
    {"$addToSet":{"entradas":  ObjectId(id_insesrcion) }}
    )
    

def updateEntradaMongo(data):
    print(data)
    print(type(data))
    now = datetime.now()
    fecha_creacion= str(now.day)+"/"+str(now.month)+"/"+str(now.year)+"   "+str(now.hour)+":"+str(now.minute)
    
    id_entrada=data[0]
    titulo=data[1]
    descripcion=data[2]
    
    #results=db.entradasTutorias.insert_one(save)
    db.entradasTutorias.update_one(
        {"_id": ObjectId(id_entrada)},
        {"$set":{"titulo":titulo,"descripcion":descripcion,"fecha_creacion":fecha_creacion}}
        )
    
    
#
#print (json_data)
    
#para mostrar resultados
#for result in results:
#    print(result)
    
    
print("Ok here")