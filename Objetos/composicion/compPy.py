"""
Que es la composicion de clases?
Es cuando tengo una clase dentro de otra.

Para que sirve la composicion de clases?
Digamos que tenemos una clase persona. Bueno, esta persona puede tener una billetera por ejemplo o unas llaves.
Estas cosas son objetos de por si tambien, con sus propias caracteristicas y comportamientos.
Por eso es mejor poder generalizarlos pues es mas facil manejarlos de esa forma.
Es una relacion de tiene-un.
"""

# Ejemplo en codigo


class Billetera:
    def __init__(self, plata):
        self.plata = plata

    def get_money(self):
        return self.plata

    def __str__(self):
        return f'Tiene: {self.plata} $ disponibles.'


class Person:

    def __init__(self, name, age, wl):
        self.name = name
        self.age = age
        self.wallet = wl

    def __str__(self):
        return f'{self.name}, {self.age}, {self.wallet}'


print(Person("william", 20, Billetera(58)))

# Es un basico ejemplo de composicion. Donde se puede ver que
# El codigo se modulariza y simplifica al tener la clase billetera.
