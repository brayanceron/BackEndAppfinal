from pymongo import MongoClient
from bson.json_util import dumps

client = MongoClient()
client = MongoClient('localhost', 27017)

db = client.BDAPPFINAL
collection = db.tutorias


pipeline = [
    {"$lookup": {"from":"profesores","localField":"id_profesor","foreignField":"_id","as":"id_profesor"}},
]


results=collection.aggregate(pipeline)
list_cur = list(results)#convirtiendo a diccionario el resultado

json_data = dumps(list_cur)#convirtiendo a json el diccionario anterior
print (json_data)
    
#para mostrar resultados
#for result in results:
#    print(result)
    
    
print("Ok here")