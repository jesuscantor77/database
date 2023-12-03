from pymongo import MongoClient
from bson.regex import Regex

client = MongoClient('mongodb://localhost:27017/')
db = client['torneo_deportivo']
posiciones = db["posiciones"]

def get_posiciones():
    return list(posiciones.find({}, {"_id": 0}))

def get_equipos():
    equipos = list(posiciones.find({}, {"_id": 0, "equipo": 1}))
    return equipos

def get_posicion_by_name(name):
    find = posiciones.find_one({"equipo": Regex(name, 'i')}, {"_id": 0})
    if find == None:
        print("No se encontro el equipo "+name+" en la tabla de posiciones")
        return 0
    return find

def get_posicion_by_regex(name):
    find = list(posiciones.find({"equipo": Regex(name, 'i')}, {"_id": 0}))
    if find == None:
        print("No se encontro el equipo "+name+" en la tabla de posiciones")
        return 0
    return find

def update_goles_encontra(name, goles):
    find = get_posicion_by_name(name)
    if find == None:
        print ("No se encontro el equipo "+name+" en la tabla de posiciones")
        return 0 
    goles = int(find["GC"]) + goles
    update = posiciones.update_one({"equipo": name}, {"$set": {"GC": goles}})
    return update.modified_count

def update_goles_favor(name, goles):
    find = get_posicion_by_name(name)
    if find == None:
        print ("No se encontro el equipo "+name+" en la tabla de posiciones")
        return 0 
    goles = int(find["GF"]) + goles
    update = posiciones.update_one({"equipo": name}, {"$set": {"GF": goles}})
    return update.modified_count

def update_game(name, status):
    find = get_posicion_by_name(name)
    pj = int(find["PJ"]) + 1
    if status == "G":
        pg = int(find["PG"]) + 1
        puntos = int(find["puntos"]) + 3
        update = posiciones.update_one({"equipo": name}, {"$set": {"PG": pg, "puntos": puntos, "PJ": pj}})
    elif status == "E":
        pe = int(find["PE"]) + 1
        puntos = int(find["puntos"]) + 1
        update = posiciones.update_one({"equipo": name}, {"$set": {"PE": pe, "puntos": puntos, "PJ": pj}})
    else :
        pp = int(find["PP"]) + 1
        puntos = int(find["puntos"])
        update = posiciones.update_one({"equipo": name}, {"$set": {"PP": pp, "puntos": puntos, "PJ": pj}})

    return update.modified_count

def insert_new_position(new_positions):
    if not isinstance(new_positions, list) or not all(isinstance(pos, dict) for pos in new_positions):
        raise TypeError('new_positions debe ser una lista de diccionarios')
    delete = posiciones.delete_many({})
    if delete.deleted_count > 0:
        return posiciones.insert_many(new_positions)