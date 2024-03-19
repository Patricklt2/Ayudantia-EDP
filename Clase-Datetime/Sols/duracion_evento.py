"""
Duración de eventos:
Hacer un programa que pida al usuario que introduzca la fecha y hora de inicio, y la fecha y
hora de finalización de un evento, y calcule la duración total del evento en horas y minutos.
"""

import datetime


def dur_evento():
    try:
        inicio = datetime.datetime.fromisoformat(input("Ingrese fecha y hora en formato YYYY-MM-DDThh:mm:ss"))
        fin = datetime.datetime.fromisoformat(input("Ingrese fecha de fin en formato YYYY-MM-DDThh:mm:ss"))

        aux = fin - inicio
        print("Hours: ", aux.days*24 + aux.seconds/3600, " Minutes: ", (aux.seconds % 3600) / 60)
    except IOError:
        print("Error de input")


dur_evento()
