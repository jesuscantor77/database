from pymongo import MongoClient
from bson.regex import Regex

client = MongoClient('mongodb://localhost:27017/')
db = client['torneo_deportivo']
entrenadores = db["entrenadores"]

def get_all_entrenadores():
    return list(entrenadores.find({}, {"_id": 0}))

def get_entrenador_by_name(name):
    return list(entrenadores.find({"nombre": Regex(name, 'i')}, {"_id": 0}))

def delete_entrenador(name):
    delete = entrenadores.delete_one({"nombre": name})
    return delete.deleted_count

def add_entrenador(entrenador):
    insert = entrenadores.insert_one(entrenador)
    return insert
