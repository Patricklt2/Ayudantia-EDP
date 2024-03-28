""" Hay varios tipos de numeros en python.
    Entre ellos los enteros, los float (reales), los complejos (a + bi) y por ultimo los decimales
"""

# algunas cosas utiles para trabajar con numeros

a = "1990"
b = "1990.01"
c = int(a)
# Estas funciones convierten un string numerico a un valor entero o real respectivamente
# Son utiles si estas trabajando con strings y tenes que extaer datos numericos
print(int(a))
print(float(b))

# todas las operaciones matematicas normales funcionan con estos numeros
print(c**2)
print(c*2)
print(++c + 3)
print(--c - 9)
print(c > 0)
