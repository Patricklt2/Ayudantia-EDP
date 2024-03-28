"""
Una clase es la descripcion de un objeto basicamente. Indica que va a poder hacer. Que caracteristicas va a tener.
Y otorga funcionalidades. Es decir, es como un molde.
Una clase tiene atributos (caracteristicas) y metodos (comportamiento)
Dentro de los metodos estan los metodos primitivos que todas las clases tienen.
Entre ellos; el __init__ , el __str__, el __eq__, el __add__, el __sub__, el __del_, el __hash__ ... y etc
Estos son los metodos rudimentarios de cada clase y son metodos que la gran mayoria de los objetos tienen en comun
si bien pueden estar implementados de formas distintas
Son especiales y muy importantes.
"""


# Estructura general de una clase en python
# class nameOfClass( SuperClass --> [solo si tiene una clase padre] ):
# variables de clase (pueden ser accedidas por todas las instancias de esa clase)
# __init__
# attributes
# methods
# Guardar archivos ej Person.py (nombre de la clase)
###


# Ejemplo

class Person:
    instance_count = 0  # class variable

    def __init__(self, name, age):
        Person.increment_instance_count()
        self.name = name
        self.age = age

# Funcion estatica que puede ser llamada fuera de la clase as in Person.static_function()
    @staticmethod
    def static_function():
        print('Static method')
    @classmethod
    def increment_instance_count(cls):
        cls.instance_count += 1
    def get_name(self):
        return self.name

    def is_teenager(self):
        return self.age < 20

    def get_age(self):
        return self.age

    def __str__(self):
        return f'{self.name} is {self.age} years'

    def __del__(self):
        Person.instance_count -= 1


p1 = Person("John", 21)
p2 = Person("Mark", 60)

print(p1.get_name())
print(int(p2.get_age()))
print(p1)
print(Person.instance_count)

# Limpieza de objs, elimina las referencias a los objetos creados
del p1
del p2

print(Person.instance_count)