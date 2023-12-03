from flask import jsonify
from modules.arbitros.model import *

def get_arbitros(nombre = ''):
    valor = []
    num = 1
    if nombre != '':
        result = get_arbitros_by_name(nombre)
        if len(result) == 0:
            print ("No se encontro en la base de datos, por favor verifica el nombre")
        else:
            for i in result:
                if i['partidos'] == 0:
                    print("Su nombre es "+i['nombre']+" es de "+i['pais']+", ha dirigido "+str(i['partidos'])+" partidos")
                else :
                    print("Su nombre es "+i['nombre']+" es de "+i['pais']+", ha dirigido "+str(i['partidos'])+" partidos, durante los cuales ha sacado "+str(i['tarjetas'])+" tarjetas")
                num = num + 1
    else:
        result = all_arbitros()
        contador = len(result)
        print ("Estos son todos los "+str(contador)+" arbitros: ")
        for i in result:
            if i['partidos'] == 0:
                print("arbitro, numero "+str(num)+". Su nombre es "+i['nombre']+" es de "+i['pais']+", ha dirigido "+str(i['partidos'])+" partidos")
            else :
                print("arbitro, numero "+str(num)+". Su nombre es "+i['nombre']+" es de "+i['pais']+", ha dirigido "+str(i['partidos'])+" partidos, durante los cuales ha sacado "+str(i['tarjetas'])+" tarjetas")
            num = num + 1
        return valor

def eliminar_arbitros(nombre = ''):
    delete_arbitro(nombre)
    return jsonify({"status": "ok"})

def agregar_arbitros(data):
    add_arbitro(data['nombre'], data['edad'], data['nacionalidad'], data['tipo'], data['partidos'])
    return jsonify({"status": "ok"})