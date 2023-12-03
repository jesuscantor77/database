from flask import jsonify
from modules.entrenadores.model import *


def get_entrenadores(nombre = ''):
    num = 1
    if nombre != '':
        result = get_entrenador_by_name(nombre)
        if len(result) == 0:
            print ("\n"+"No se encontro en la base de datos, por favor verifica el nombre \n")
        else:
            contador = len(result)
            if contador == 1:
                print ("\n"+"Se encontro "+str(contador)+" entrenador: \n")
            else:
                print ("\n"+"Se encontraron "+str(contador)+" entrenadores: \n")
            for i in result:
                print("Su nombre es "+i['nombre']+" dirige actualmente al "+i['equipo'])
    else:
        result = get_all_entrenadores()
        contador = len(result)
        print ("\n"+"Estos son todos los "+str(contador)+" entrenadores: \n")
        for i in result:
            print("Su nombre es "+i['nombre']+" dirige actualmente al "+i['equipo'])
            num = num + 1
    

def eliminar_entrenadores(nombre):
    delete_entrenador(nombre)
    return jsonify({"status": "ok"})


def agregar_entrenadores(data):
    add_entrenador(data['nombre'], data['equipo'])
    return jsonify({"status": "ok"})