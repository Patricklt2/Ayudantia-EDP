"""
La idea de usar composicion de clases es tanto para retener la individualidad de cada objeto como para hacerlo mas
legible o facil de entender.
Un muy buen ejemplo es la composicion Autor x Libro x Biblioteca
"""


class Autor:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# Un libro tiene autores
class Libro:
    def __init__(self, titulo, autores):
        self.titulo = titulo
        self.autores = autores

    def __str__(self):
        autores_str = ", ".join(str(autor) for autor in self.autores)
        return f"Libro: {self.titulo}, Autores: {autores_str}"


# Una biblioteca tiene libros
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def __str__(self):
        libros_str = "\n".join(str(libro) for libro in self.libros)
        return f"Biblioteca: {self.nombre}\n{libros_str}"


# Ejemplo de uso
autor1 = Autor("Juan", "García")
autor2 = Autor("María", "López")
libro1 = Libro("Python para principiantes", [autor1])
libro2 = Libro("Introducción a la programación en Python", [autor1, autor2])

biblioteca = Biblioteca("Biblioteca Central")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

print(biblioteca)
