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


# Un ejemplo mas "complejo"
