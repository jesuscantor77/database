from modules.partidos.model import *

def get_partidos(equipo):
    result = get_partidos_by_equipo(equipo)
    if len(result) == 0:
        print ("\n"+"No se encontro en la base de datos, por favor verifica el nombre")
    else:
        print ("\n"+"Los partidos del "+equipo+" son los siguientes: \n")
        for i in result:
            jornadas = str(i['jornada'])
            partidos = i['partidos']
            for p in partidos:
                if p['local'].lower() == equipo:
                    print("El "+p['local']+" jugara contra "+p['visitante']+ " en la jornada "+jornadas)
                elif p['visitante'].lower() == equipo:
                    print("El "+p['local']+" jugara contra "+p['visitante']+ " en la jornada "+jornadas)
        
    
