"""
Ahora entramos al mundo de es-un. En particular herencia simple y multiple.
La herencia multiple no es la mejor practica pues puede causar problemas.
Normalmente se utiliza la herencia simple, pero hay casos en los que la herencia multiple tiene sentido.
La idea de la herencia es reciclar codigo y comportamientos
"""

# Sintaxis para definir subclases o mas bien hijos
# class SubClassName(BaseClassName):  BaseClassName es la clase padre


# Ejemplo Person x Employee x SalesPerson

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        print('Happy birthday you were', self.age)
        self.age += 1
        print('You are now', self.age)


class Employee(Person):
    def __init__(self, name, age, ids):
        super().__init__(name, age)
        self.id = ids

    def calculate_pay(self, hours_worked):
        rate_of_pay = 7.50

        if self.age >= 21:
            rate_of_pay += 2.50
        return hours_worked * rate_of_pay


class SalesPerson(Employee):
    def __init__(self, name, age, ids, region, sales):
        super().__init__(name, age, ids)
        self.region = region
        self.sales = sales

    def bonus(self):
        return self.sales * 0.5

# Donde Person es la superclass, employee es la class y la subclass es SalesPerson
# (Una version mas especifica de Employee)
# Existe e multiple class inheritance ej Toy & Car


class Car:
    def move(self):
        print('Car - move()')


class Toy:
    def move(self):
        print('Toy - move()')


class ToyCar(Car, Toy):
    def __init__(self):
        super().__init__()


tc = ToyCar()
tc.move()

# Como el algoritmo usa el breadth First Search va a agarrar el metodo move de car en vez de el de toy
# Si fuera class ToyCar(Toy, Car) agarraria primero el de toy en vez de el de car. Si no estuviera en ellos
# Agarraria el de object (Esto es siempre y cuando no se vea sobreescrito dentro de la clase ToyCar
