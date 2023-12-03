from bson import ObjectId
from pymongo import MongoClient
from bson.regex import Regex

client = MongoClient('mongodb://localhost:27017/')
db = client['torneo_deportivo']
if "jornadas" not in db.list_collection_names():
    db.create_collection("jornadas")
jornada = db["jornadas"]

def get_jornada_by_number(number):
    return list(jornada.find({"jornada": number}))

def get_jornada():
    find = jornada.find({})
    return list(find)

def update_jornada(number, num_partido, jornada):
    update = jornada.update_one({"jornada": number, "partido": num_partido}, {"$set": {"resultado": jornada}})
    return update.modified_count

def insert_jornada(jornada):
    return jornada.insert_one(jornada)

def inset_partidos_by_jornada(jornada_id, local, visitante, golesLocal, golesVisitante):
    return jornada.insert_one({"jornada": jornada_id, "partidos": [{"local": local, "visitante": visitante, "golesLocal": golesLocal, "golesVisitante": golesVisitante}]})

def update_jornada_by_id(_id, array_datos):
    return jornada.update_one({"_id": ObjectId(_id)}, {"$set": {"partidos": array_datos}})