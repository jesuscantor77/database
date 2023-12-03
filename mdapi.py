from generate import sync
from model import *
from insert import *

insert()
sync()
print("\n"+"Bienvenido a la beta de soccer emulators, si quieres saber como se llaman los equipos, puedes escribir tabla para ver la tabla de posiciones ")
text = input("Escribe una de las opciones que quieras buscar: arbitros, jugadores, entrenadores, tabla, partidos: ")

if text != '':
    buscar(text)
else:
    print("No has introducido una accion valida, Recuerda escribir una de las siguientes opciones: arbitros, jugadores, entrenadores, tabla, partidos")

