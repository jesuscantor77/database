import pymongo
from bson.regex import Regex

ports = [27017, 27018, 27019]
replica_set = 'rs0'

for port in ports:

    client = pymongo.MongoClient(f"mongodb://localhost:{port}/replicaSet={replica_set}")
    db = client['torneo_deportivo']
    jornada = db["jornadas"]

    def get_partidos_by_equipo(equipo):
        partidos  = list(jornada.find({"$or": [{"partidos.local": Regex(equipo, 'i')}, {"partidos.visitante": Regex(equipo, 'i')}]}, {"_id": 0}))
        return partidos