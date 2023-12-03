import pymongo
from pymongo.errors import CollectionInvalid
import json

ports = [27017, 27018, 27019]
replica_set = 'rs0'

for port in ports:

    client = pymongo.MongoClient(f"mongodb://localhost:{port}/replicaSet={replica_set}")

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