from flask import jsonify
from modules.jornada.model import *

def get_jornada_equipos(jornada):

    if jornada not in (1, 2):
        print ("\n"+"No se encontro en la base de datos, por favor recuerda que solo hay 2 jornadas disponibles y que el numero de jornada debe ser 1 o 2 \n")
        return
    result = get_jornada_by_number(int(jornada))
    if result is None:
        print ("\n"+"No se encontro en la base de datos, por favor recuerda que solo hay 2 jornadas disponibles y que el numero de jornada debe ser 1 o 2 \n")
        return
    else:
        print ("\n"+"Los resultados de los partidos de la jornada "+str(jornada)+" son los siguientes: \n")
        for i in result:
            partidos = i['partidos']
            for p in partidos:
                if p['golesLocal'] > p['golesVisitante']:
                    print("El "+p['local']+" gano contra "+p['visitante']+" por "+str(p['golesLocal'])+" a "+str(p['golesVisitante'])+" y el arbitro fue "+p['arbitro'])
                else:
                    print("El "+p['visitante']+" gano contra "+p['local']+" por "+str(p['golesVisitante'])+" a "+str(p['golesLocal'])+" y el arbitro fue "+p['arbitro'])
                

def insert_time_jornada(data):
    insert_jornada(data['jornada'], data['local'], data['visitante'], data['estadio'], data['hora'], data['fecha'])