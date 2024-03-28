"""
Un ejemplo mas, por ahi hasta mas entendible que el anterior, ya que ese tenia muchos numeros o requisitos.
"""


class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __eq__(self, other):
        return self.nombre == other.nombre and self.edad == other.edad


class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def ladrar(self):
        print("¡Guau!")


class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    def maullar(self):
        print("¡Miau!")


# Ejemplo de uso
perro1 = Perro("Fido", 3, "Labrador")
perro2 = Perro("Fido", 3, "Pastor Alemán")
gato1 = Gato("Whiskers", 5, "Gris")
gato2 = Gato("Garfield", 6, "Naranja")

print(perro1 == perro2)  # True, ya que tienen el mismo nombre y edad. Se podria agregar que tambien verifique
                        # raza y o color dependiendo de si esta en perro o gato, sobreescribiendo el __eq__ y usando
                        # lo que ya esta escrito en el padre
print(gato1 == gato2)  # False, ya que tienen nombres y edades diferentes

"""
    Por ejemplo:
    
    en perro:
    ...
    def __eq__(self, other):
        return super().__eq__(other) and self.raza == other.raza
        
    de esa forma mantengo el codigo que ya compara nombre y edad (en el padre) y solo agrego que en el hijo
    compare la raza tambien
"""