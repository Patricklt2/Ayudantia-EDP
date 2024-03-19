"""
Contador de tiempo transcurrido:
Programa que cree un contador de tiempo transcurrido que muestre cuánto tiempo ha pasado desde que
se inició el programa.
"""
from datetime import time, datetime, timedelta


def time_counter():
    aux = datetime.now()
    time_ini = time(aux.hour, aux.minute, aux.second)

    while True:
        if input("Ingrese cualquier cosa") != '\0':
            break

    aux_f = datetime.now()
    time_fin = time(aux_f.hour, aux_f.minute, aux_f.second)

    print(time_fin.second - time_ini.second)


time_counter()
