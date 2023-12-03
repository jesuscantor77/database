import pymongo
from bson.regex import Regex

ports = [27017, 27018, 27019]
replica_set = 'rs0'

for port in ports:

    client = pymongo.MongoClient(f"mongodb://localhost:{port}/replicaSet={replica_set}")
    db = client['torneo_deportivo']
    arbitros = db["arbitros"]

    def all_arbitros():
        return list(arbitros.find({}, {"_id": 0}))

    def get_arbitros_by_name(name):
        return list(arbitros.find_one({"nombre": Regex(name, 'i')}, {"_id": 0}))

    def delete_arbitro(name):
        delete = arbitros.delete_one({"nombre": name})
        return delete.deleted_count

    def add_arbitro(arbitro):
        insert = arbitros.insert_one(arbitro)
        return insert

    def update_arbitro(name):
        get = arbitros.find_one({"nombre": name})
        if get != None:
            partidos = int(get['partidos']) + 1
            update = arbitros.update_one({"nombre": name}, {"$set": {"partidos": partidos}})
            return update.modified_count
        
    def insert_arbitro(arbitro):
        if not isinstance(arbitro, list) or not all(isinstance(pos, dict) for pos in arbitro):
            raise TypeError('new_positions debe ser una lista de diccionarios')
        delete = arbitros.delete_many({})
        if delete.deleted_count > 0:
            return arbitros.insert_many(arbitro)