from pymongo import MongoClient
from bson.regex import Regex

client = MongoClient('mongodb://localhost:27017/')
db = client['torneo_deportivo']
jornada = db["jornadas"]

def get_partidos_by_equipo(equipo):
    partidos  = list(jornada.find({"$or": [{"partidos.local": Regex(equipo, 'i')}, {"partidos.visitante": Regex(equipo, 'i')}]}, {"_id": 0}))
    return partidos