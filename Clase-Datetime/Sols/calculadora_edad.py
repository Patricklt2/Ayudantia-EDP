"""
Calculadora de edad:
Hacer un programa que pida al usuario que introduzca
su fecha de nacimiento y calcule su edad en años, meses y días.
Tomando un mes como 28 dias
"""

from datetime import date


def calculadora_edad():
    try:
        cumple = date.fromisoformat(input("Ingrese su fecha de cumple en formato YYYY-MM-DD"))
        dia_de_hoy = date.today()

        print("Years: ", (dia_de_hoy - cumple).days/365, " Months: ", (dia_de_hoy - cumple).days/28, " Days: ",
              (dia_de_hoy - cumple).days)
    except ValueError:
        print("Error")


calculadora_edad()
