from flask import jsonify
from modules.deportistas.model import *

def get_deportistas(nombre = ''):
    num = 1
    if nombre != '':
        result = get_deportista_by_name(nombre)
        if len(result) == 0:
            print ("\n"+"No se encontro en la base de datos, por favor verifica el nombre \n")
        else:
            for i in result:
                print("Su nombre es "+str(i['nombre'])+" tiene el dorsal #"+str(i['dorsal'])+", juega de "+str(i['tipo'])+" en el "+str(i['equipo']))
                num = num + 1
    else:
        result = get_jugadores()
        contador = len(result)
        print ("\n"+"Se encontraron "+str(contador)+" jugadores: \n")

        for i in result:
            print("Su nombre es "+str(i['nombre'])+" tiene el dorsal #"+str(i['dorsal'])+", juega de "+str(i['tipo'])+" en el "+str(i['equipo']))
            num = num + 1
    

def eliminar_deportistas(nombre):
    delete_deportista(nombre)
    print ("El jugador ha sido eliminado")


def agregar_deportistas(data):
    add_deportista(data['nombre'], data['edad'], data['nacionalidad'], data['tipo'], data['equipo'])
    print ("El jugador ha sido agregado")


def actualizar_deportistas(data):
    update_deportista(data['nombre'], data['edad'], data['nacionalidad'], data['tipo'], data['equipo'])
    print ("El jugador ha sido actualizado")


def actualizar_lesionados(data):
    update_deportista(data['nombre'], data['lesionado'])
    print ("La lesion del jugador ha sido actualizada")


def actualizar_sancionados(data):
    update_sancionado(data['nombre'], data['tarjetas'])
    print ("El jugador ha sido sancionado")