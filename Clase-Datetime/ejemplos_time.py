from datetime import time, timezone

# Algunas formas para crear objetos time

tiempo1 = time(6, 7, 6, 9, tzinfo=None)
tiempo2 = time.fromisoformat('04:23:01')

print(tiempo2)

# Comparaciones

tiempo1 = tiempo1.replace(8)

if tiempo1 > tiempo2:
    print(tiempo1)

tiempo1 = tiempo1.replace(tzinfo=timezone.utc)

# Imprimir e imprimir con formato

print(tiempo1.__str__())
tiempo2.strftime("%H:%M:%S %Z")
print(tiempo1.tzname())

# Ejemplo mas complejo

