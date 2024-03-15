from datetime import date

# Algunas formas para crear objetos date

fecha1 = date(2002, 4, 14)

fecha3 = date.today()

fecha2 = date.fromisoformat("2002-04-14")

# Las comparaciones normales funcionan

if fecha1 == fecha2:
    print(fecha1)

if fecha3 > fecha2:
    print(fecha3)

# Imprime la diferencia en dias y horas

print(fecha3 - fecha1)

fecha3 = fecha3.replace(year=2002)
print(fecha3 - fecha1)

print(fecha1.__str__())

# Para imprimir con formato
print(fecha1.strftime("%Y/%m/%d"))

# Tambien es valido

print(fecha1.year, "/", fecha1.month, "/", fecha1.day)

# Un ejemplo mas "complejo"
""" Se requiere un programa que pueda convertir una fecha del formato YYYY-MM-DD a YYYY/MM/DD. 
Ademas el programa debe filtrar cualquier fecha antes del 2017 y despues del 2021, Solo aceptando como validas 
las fechas en medio. Se garantiza que las fechas seran ingresadas en el formato YYYY-MM-DD."""

"""
def prog(d):
    try:
        d1 = date.fromisoformat(d)

        if d1.year >= 2017 and d1.year <= 2021:
            return d1.strftime("%Y/%m/%d")
        else:
            print("Invalid Date")

    except:
        print("Formato invalido")


d = "y"

while d != "n":
    d = input("Introduzca una fecha ")
    print(prog(d.__str__()))
"""