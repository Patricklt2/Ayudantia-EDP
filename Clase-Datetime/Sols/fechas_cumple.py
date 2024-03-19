"""
Fechas de cumpleaños:
Hacer un programa que pida al usuario que introduzca fechas de cumpleaños de varios amigos y
familiares, y luego ordene estas fechas en orden cronológico.
"""
from datetime import date


def ordenador_fechas():
    try:
        lista = []
        while True:
            looped = input("Ingrese su fecha de cumple en formato YYYY-MM-DD ")
            if looped != "n":
                lista.append(date.fromisoformat(looped))
            else:
                break

        lista.sort(reverse=True)
        print(lista)

    except IOError:
        print("error")


ordenador_fechas()
