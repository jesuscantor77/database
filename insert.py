from pymongo import MongoClient
from pymongo.errors import CollectionInvalid
import json

client = MongoClient('mongodb://localhost:27017/')

db = client['torneo_deportivo']

def insert():
    with open('insert.json') as f:
        data = json.load(f)
        for i in data:
            if i == 'entrenador':
                entrenador = data[i]
                try:
                    collection = db.create_collection('entrenadores')
                    collection.insert_many(entrenador)
                except CollectionInvalid:
                    collection = db['entrenadores']
                    collection.delete_many({})
                    collection.insert_many(entrenador)
            elif i == 'jugadores':
                jugador = data[i]
                try:
                    collection = db.create_collection('jugadores')
                    collection.insert_many(jugador)
                except CollectionInvalid:
                    collection = db['jugadores']
                    collection.delete_many({})
                    collection.insert_many(jugador)
            elif i == 'arbitros':
                arbitro = data[i]
                try:
                    collection = db.create_collection('arbitros')
                    collection.insert_many(arbitro)
                except CollectionInvalid:
                    collection = db['arbitros']
                    collection.delete_many({})
                    collection.insert_many(arbitro)
            elif i == 'tabla':
                tabla = data[i]
                try:
                    collection = db.create_collection('posiciones')
                    collection.insert_many(tabla)
                except CollectionInvalid:
                    collection = db['posiciones']
                    collection.delete_many({})
                    collection.insert_many(tabla)
            elif i == 'jornadas':
                tabla = data[i]
                try:
                    collection = db.create_collection('jornadas')
                    collection.insert_many(tabla)
                except CollectionInvalid:
                    collection = db['jornadas']
                    collection.delete_many({})
                    collection.insert_many(tabla)