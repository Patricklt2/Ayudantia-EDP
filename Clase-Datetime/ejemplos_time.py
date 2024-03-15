from datetime import time, timezone

# Algunas formas para crear objetos time

tiempo = time(10, 30, 15)
tiempo3 = time.fromisoformat('04:23:01')
print("Tiempo:", tiempo)

# Acceder a las partes individuales del tiempo
print("Hora:", tiempo.hour)
print("Minuto:", tiempo.minute)
print("Segundo:", tiempo.second)

# Formatear el tiempo como una cadena
print("Formato de 24 horas:", tiempo.strftime("%H:%M:%S"))
print("Formato de 12 horas:", tiempo.strftime("%I:%M:%S %p"))

# Comparar tiempos
tiempo1 = time(10, 30, 15, tzinfo=None)
tiempo2 = time(12, 45, 30)

if tiempo1 < tiempo2:
    print("El tiempo 1 < tiempo 2")
elif tiempo1 == tiempo2:
    print("Los tiempos son ==")
else:
    print("El tiempo 2 < tiempo 1")

tiempo1 = tiempo1.replace(tzinfo=timezone.utc)
print(tiempo1.tzname())
