from pymongo import *
import json

# Me conecto a la base de datos
client = MongoClient('localhost', 27017)
db = client['airlines']

# Elimino la coleccion para que no se dupliquen documentos al cargar
db.drop_collection("airlines")

# Cargo el archivo con mis datos en memoria
f = open('airlines.json', 'r')
documents = json.loads(f.read()) # Convierto un string a objeto de python

# Creo la coleccion
collection = db.airlines

# Cargar todos los documentos en la coleccion
collection.insert_many(documents)


# Cuantos documentos hay en total?
documents = collection.find({})  # Consulta vacia, retorna todos los documentos
c = 0
for doc in documents:
    c +=1
print (c)

# Cuantos aeropuertos existen en total?


# Cuantos vuelos en los aeropuertos de Miami ("code": "MIA") estuvieron retrasados (delayed)?
consulta = {
    "airport.code": "MIA"   # Asi se consulta por campos anidados
}
documents = collection.find(consulta)
c = 0
for doc in documents:
    # do something...
print (c)

# En que mes de entre todos los anios en todos los aeropuertos se cancelaron (canceled) mas vuelos?

# Que aerolinea tuvo mas vuelos atrasados? (delayed)

# Que aerolinea es la mejor? (Menor proporcion de vuelos cancelados + atrasados/vuelos totales)