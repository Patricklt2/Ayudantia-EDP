"""
Organizador / filtro de fechas:
Dado el siguiente archivo se desea filtrar todos libros creados antes del 2017-04-14 y luego del 2021-05-25.
Se garantiza que la primer columna del csv tiene fechas validas en formato "YYYY-MM-DD" y que la segunda columna del csv
tiene los nombres de libros.
El programa debe imprimir a pantalla con su fecha los libros en el siguiente formato: "Libro" "YYYY/MM/DD".
Ademas los libros con fecha en 2019-06-01 a 2019-09-30 estan mal marcados, enrealidad su fecha es 2020;
Por lo que se debe corregir antes de imprimir a pantalla.
**IMPORTANTE** Se debe realizar UNA sola pasada
"""
from datetime import date
import csv


def filtro_de_fechas():

    filtro1 = date(2017, 4, 12)
    filtro2 = date(2021, 5, 25)

    filtro3 = date(2019, 6, 1)
    filtro4 = date(2019, 9, 30)

    try:
        with open("books.txt", 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                f_aux = date.fromisoformat(row[0])
                if filtro1 <= f_aux <= filtro2:
                    if filtro3 <= f_aux <= filtro4:
                        # Aca tambien se podria haber puesto directamente 2020/%m/%d
                        print('"', row[1], '"', ' "', f_aux.replace(year=2020).strftime("%Y/%m/%d"), '"')
                    else:
                        print('"', row[1], '"', ' "', f_aux.strftime("%Y/%m/%d"), '"')
    except FileNotFoundError:
        print("No existe el archivo")


filtro_de_fechas()
