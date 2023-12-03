from modules.arbitros.control import get_arbitros
from modules.deportistas.control import get_deportistas
from modules.entrenadores.control import get_entrenadores
from modules.partidos.control import get_partidos
from modules.tabla.control import get_tabla
from modules.jornada.control import get_jornada_equipos

def buscar(data):
    if data == 'arbitros':
        buscar = input("\n"+"Deseas buscar un arbitro en concreto? (si, no): ")
        if buscar == 'si':
            nombre = input("\n"+"Introduce el nombre del arbitro: ")
            print("Este es el resultado que ha coincidido con tu busqueda de arbitros: \n")
            get_arbitros(nombre.lower())
        elif buscar == 'no':
            print("Estos son todos los arbitros: ")
            get_arbitros()
        else:
            print("\n"+"No has introducido una accion valida, Recuerda Las acciones validas son: si, no \n")
            
    elif data == 'jugadores':
        buscar = input("\n"+"Deseas buscar un jugador en concreto? (si, no): ")
        if buscar == 'si':
            nombre = input("\n"+"Introduce el nombre del jugador: ")
            print("Este es el resultado que ha coincidido con tu busqueda de jugadores: \n")
            get_deportistas(nombre.lower())
        elif buscar == 'no':
            get_deportistas()
        else:
            print("\n"+"No has introducido una accion valida, Recuerda Las acciones validas son: si, no \n")

    elif data == 'entrenadores':
        buscar = input("\n"+"Deseas buscar un entrenador en concreto? (si, no): ")
        if buscar == 'si':
            nombre = input("\n"+"Introduce el nombre del entrenador: ")
            get_entrenadores(nombre.lower())
        elif buscar == 'no':
            get_entrenadores()
        else:
            print("\n"+"No has introducido una accion valida, Recuerda Las acciones validas son: si, no \n")

    elif data == 'tabla':
        buscar = input("\n"+"Deseas ver la posicion de un equipo en concreto? (si, no): ")
        if buscar == 'si':
            equipo = input("Introduce el nombre del equipo: ")
            get_tabla(equipo.lower())
        elif buscar == 'no':
            get_tabla()
        else:
            print("\n"+"No has introducido una accion valida, Recuerda Las acciones validas son: si, no \n")

    elif data == 'partidos':
        buscar = input("\n"+"Deseas ver los partidos de alguna jornada en concreto? (si, no): ")
        if buscar == 'si':
            jornada = input("\n"+"Introduce el numero de la jornada: (Disponibles, jornadas 1 y 2) " )
            get_jornada_equipos(int(jornada))
        elif buscar == 'no':
            buscar = input("Introduce el nombre del equipo: (tienes que introducir el equipo a buscar): ")
            if buscar != '':
                get_partidos(buscar.lower())
            else:
                print("\n"+"No has introducido una accion valida, Recuerda introducir el nombre del equipo \n")
        else:
            print("\n"+"No has introducido una accion valida, Recuerda Las acciones validas son: si, no \n")

    else:
        print("\n"+"No has introducido una accion valida, Recuerda Las acciones validas son: arbitros, deportistas, entrenadores, tabla, partidos \n")

