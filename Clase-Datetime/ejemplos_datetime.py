from datetime import datetime, date, time, timezone

# Formas de crear datetime

date1 = datetime(2023, 4, 14, 8,45)

date2 = datetime.now()

date3 = datetime.today()

date4 = datetime.combine(date(2007,6,7), time(7,47), timezone.utc)

date5 = datetime.fromisoformat('2011-11-04T00:05:23Z')

print(date5)
print(date1.__str__())

# Las comparaciones funcionan igual
print(date3 == date2)


# Metodos de retorno de atributos de forma individual

print(date4.date())
print(date4.time())
print(date4.timetz())


date4 = date4.replace(year=2019, month=1)

# Permite convertir datetime a otra timezone
print(date4.astimezone(tz=timezone.max))

# Imprimir con formato # Hay mas formatos posibles
print(date2.strftime('%A, %d. %B %Y %I:%M%p'))

# Ejemplo mas complejo
