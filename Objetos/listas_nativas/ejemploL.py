class Pelicula:
    def __init__(self, titulo, genero, stock):
        self.titulo = titulo
        self.genero = genero
        self.stock = stock

    def __str__(self):
        return f"{self.titulo} - {self.genero} (Stock: {self.stock})"


class TiendaDePeliculas:
    def __init__(self):
        self.stock_peliculas = []

    def agregar_pelicula(self, pelicula):
        self.stock_peliculas.append(pelicula)

    def rentar_pelicula(self, titulo):
        for pelicula in self.stock_peliculas:
            if pelicula.titulo == titulo:
                if pelicula.stock > 0:
                    pelicula.stock -= 1
                    print(f"¡Se rentó la película '{pelicula.titulo}'!")
                else:
                    print("Lo sentimos, la película no está disponible en este momento.")
                return
        print("Lo sentimos, no encontramos la película que estás buscando.")

# Crear algunas películas
pelicula1 = Pelicula("El Padrino", "Drama", 3)
pelicula2 = Pelicula("Interestelar", "Ciencia Ficción", 5)
pelicula3 = Pelicula("Toy Story", "Animación", 2)

# Crear una tienda de películas y agregar películas al stock
tienda = TiendaDePeliculas()
tienda.agregar_pelicula(pelicula1)
tienda.agregar_pelicula(pelicula2)
tienda.agregar_pelicula(pelicula3)

# Rentar películas
tienda.rentar_pelicula("Interestelar")
tienda.rentar_pelicula("El Padrino")
tienda.rentar_pelicula("Toy Story")
tienda.rentar_pelicula("El Padrino")  # Intentar rentar una película que no está en stock
