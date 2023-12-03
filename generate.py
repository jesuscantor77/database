from modules.jornada.model import *
from modules.arbitros.control import *
from modules.tabla.model import *
import random

def sync():
    array_partidos = []
    array_id = []
    arbitros_name = []
    data_arbitros = []
    equipos = []
    new_posicion = []
    position = 1

    allArbitros = all_arbitros()
    for a in allArbitros:
        arbitros_name.append(a['nombre'])
        data_arbitros.append({"nombre": a['nombre'], "pais": a['pais'], "tarjetas": a['tarjetas'], "partidos": a['partidos']})


    jornada = get_jornada()
    if jornada != None:
        jornada_int = jornada
        for i in jornada_int:
            partidos = i['partidos']
            jornadas = i['jornada']
            if jornadas == 1:
                for p in partidos:
                    marcador_local = random.randint(0, 5)
                    marcador_visitante = random.randint(0, 5)
                    if marcador_local > marcador_visitante:
                        local_status = "G"
                        visitante_status = "P"
                    elif marcador_local < marcador_visitante:
                        local_status = "P"
                        visitante_status = "G"
                    else:
                        local_status = "E"
                        visitante_status = "E"
                    arbitro = random.choice(arbitros_name)
                    array_partidos.append({"local": p['local'], "visitante": p['visitante'], "golesLocal": marcador_local, "golesVisitante": marcador_visitante, "arbitro": arbitro})
                    update_arbitro(arbitro)

                    for d in data_arbitros:
                        if d['nombre'] == arbitro:
                            partidos = int(d['partidos']) + 1
                            data_arbitros[data_arbitros.index(d)]['partidos'] = partidos
                    
                    data_arbitros.sort(key=lambda x: x['partidos'], reverse=True)
                    insert_arbitro(data_arbitros)


                    update_game(p['local'], local_status)
                    update_goles_encontra(p['local'], marcador_visitante)
                    update_goles_favor(p['local'], marcador_local)

                    update_game(p['visitante'], visitante_status)
                    update_goles_encontra(p['visitante'], marcador_local)
                    update_goles_favor(p['visitante'], marcador_visitante)

                    if str(i['_id']) not in array_id:
                        array_id.append(str(i['_id']))
                    if len(array_partidos) == 10:
                        update_jornada_by_id(array_id[0], array_partidos)
                        array_partidos = []
            elif jornadas == 2:
                for p in partidos:
                    marcador_local = random.randint(0, 5)
                    marcador_visitante = random.randint(0, 5)
                    if marcador_local > marcador_visitante:
                        local_status = "G"
                        visitante_status = "P"
                    elif marcador_local < marcador_visitante:
                        local_status = "P"
                        visitante_status = "G"
                    else:
                        local_status = "E"
                        visitante_status = "E"
                    arbitro = random.choice(arbitros_name)
                    array_partidos.append({"local": p['local'], "visitante": p['visitante'], "golesLocal": marcador_local, "golesVisitante": marcador_visitante, "arbitro": arbitro})
                    update_arbitro(arbitro)

                    for d in data_arbitros:
                        if d['nombre'] == arbitro:
                            partidos = int(d['partidos']) + 1
                            data_arbitros[data_arbitros.index(d)]['partidos'] = partidos
                    
                    data_arbitros.sort(key=lambda x: x['partidos'], reverse=True)
                    insert_arbitro(data_arbitros)

                    update_game(p['local'], local_status)
                    update_goles_encontra(p['local'], marcador_visitante)
                    update_goles_favor(p['local'], marcador_local)

                    update_game(p['visitante'], visitante_status)
                    update_goles_encontra(p['visitante'], marcador_local)
                    update_goles_favor(p['visitante'], marcador_visitante)

                    if str(i['_id']) not in array_id:
                        array_id.append(str(i['_id']))
                    if len(array_partidos) == 10:
                        update_jornada_by_id(array_id[1], array_partidos)
                        array_partidos = []

    posicion = get_posiciones()
    posicion.sort(key=lambda x: x['puntos'], reverse=True)

    for i in posicion:

        for j in posicion:
            if i['puntos'] == j['puntos'] and i['equipo'] != j['equipo']:
                GD = i['GF'] - i['GC']
                GD2 = j['GF'] - j['GC']
                if GD > GD2:
                    posicion[posicion.index(i)]['position'] = posicion.index(i) + 1
                elif GD2 > GD:
                    posicion[posicion.index(j)]['position'] = posicion.index(j) + 1
                else:
                    equipos.append(j['equipo'])
                
        if len(equipos) > 1:
            for e in equipos:
                if e == i['equipo']:
                    posicion[posicion.index(i)]['position'] = equipos.index(e) + 1

    for i in posicion:
        new_posicion.append({"position": position, "equipo": i['equipo'], "PJ": i['PJ'], "PG": i['PG'], "PE": i['PE'], "PP": i['PP'], "GF": i['GF'], "GC": i['GC'], "puntos": i['puntos']})
        position += 1

    insert_new_position(new_posicion)
