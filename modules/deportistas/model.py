from pymongo import MongoClient
from bson.regex import Regex

client = MongoClient('mongodb://localhost:27017/')
db = client['torneo_deportivo']
jugadores = db["jugadores"]


def get_jugadores():
    return list(jugadores.find({}, {"_id": 0}))

def delete_deportista(name):
    delete = jugadores.delete_one({"nombre": name})
    return delete.deleted_count

def add_deportista(deportista):
    insert = jugadores.insert_one(deportista)
    return insert

def get_deportista_by_name(name):
    return list(jugadores.find({"nombre": Regex(name, 'i')}, {"_id": 0}))

def update_deportista(name, update):
    lesion = update == 'lesionado'
    if lesion:
        update = jugadores.update_one({"nombre": name}, {"$set": {"lesionado": lesion}})
        return update.modified_count
    else:
        update = jugadores.update_one({"nombre": name}, {"$set": {"edad": update["edad"], "nacionalidad": update["nacionalidad"], "tipo": update["tipo"], "equipo": update["equipo"]}})
        return update.modified_count

def update_sancionado(name, tarjetas):
    find = get_deportista_by_name(name)
    amonestacion = find["amonestacion"] + tarjetas
    sancionado = tarjetas >= 3
    if sancionado:
        update = jugadores.update_one({"nombre": name}, {"$set": {"amonestacion": amonestacion, "sancionado": sancionado}})
        return update.modified_count
    else:
        update = jugadores.update_one({"nombre": name}, {"$set": {"amonestacion": amonestacion}})
        return update.modified_count