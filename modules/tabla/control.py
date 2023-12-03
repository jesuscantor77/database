from flask import jsonify
from modules.tabla.model import *

def get_tabla(name = ''):
    if name != '':
        result = get_posicion_by_regex(name)
        if len(result) > 0:
            print ("\n"+"La tabla de posiciones es la siguiente: \n")
            for i in result:
                print("El "+i['equipo']+" esta en la posicion "+str(i['position'])+" con "+str(i['puntos'])+" puntos, ha jugador "+str(i['PJ'])
                      +" partidos, ganado "+str(i['PG'])+", empatado "+str(i['PE'])+" y perdido "+str(i['PP'])+"; ha hecho "+str(i['GF'])+" goles y recibido "+str(i['GC'])+" goles")
    else:
        result = get_posiciones()
        print ("\n"+"La tabla de posiciones es la siguiente: \n")
        for i in result:
            print("El "+i['equipo']+" esta en la posicion "+str(i['position'])+" con "+str(i['puntos'])+" puntos, ha jugador "+str(i['PJ'])
                  +" partidos, ganado "+str(i['PG'])+", empatado "+str(i['PE'])+" y perdido "+str(i['PP'])+"; ha hecho "+str(i['GF'])+" goles y recibido "+str(i['GC'])+" goles")

def update_goles_enc(data):
    update_goles_encontra(data['equipo'], data['goles'])

def update_goles_fav(data):
    update_goles_favor(data['equipo'], data['goles'])