"""A la siguiente herencia se le desea agregar una posicion inicial y la posibilidad de movimiento.
    Los vehiculos terrestres deben tener un factor de movimiento de 1. Los maritimos de 0.7. Los aereos de 1.5
    Este factor de movimiento, va a modificar que tan rapido se mueven.
    *sugerencia: En la funcion movimiento que tienen que agregar utilizar este factor en algun lado..*

    Ademas, agregar el metodo __eq__ en vehiculo para comparar los valores que tienen en comun todos los vehiculos.
    Y agregarlo en cada hijo de vehiculo, para que puedan distinguirse entre si.

    Agregar una lista a vehiculo donde se almacenen que vehiculos fueron creados. Se debe poder acceder siempre.
    *sugerencia variable de clase*

    Agregar un metodo a vehiculo donde se imprima cada item de la lista a pantalla.

"""

class Vehiculo:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def __str__(self):
        return f"{self.marca} {self.modelo} - ${self.precio}"


class VehiculoTerrestre(Vehiculo):
    def __init__(self, marca, modelo, precio, tipo_motor):
        super().__init__(marca, modelo, precio)
        self.tipo_motor = tipo_motor

    def __str__(self):
        return super().__str__() + f", Motor: {self.tipo_motor}"


class VehiculoAereo(Vehiculo):
    def __init__(self, marca, modelo, precio, tipo_alas):
        super().__init__(marca, modelo, precio)
        self.tipo_alas = tipo_alas

    def __str__(self):
        return super().__str__() + f", Tipo de Alas: {self.tipo_alas}"


class VehiculoMaritimo(Vehiculo):
    def __init__(self, marca, modelo, precio, eslora):
        super().__init__(marca, modelo, precio)
        self.eslora = eslora

    def __str__(self):
        return super().__str__() + f", Eslora: {self.eslora}"


# Ejemplo de uso
vehiculo_terrestre = VehiculoTerrestre("Toyota", "Corolla", 20000, "Gasolina")
vehiculo_aereo = VehiculoAereo("Boeing", "747", 10000000, "Jet")
vehiculo_maritimo = VehiculoMaritimo("Yamaha", "WaveRunner", 8000, "3m")

print("Vehículo Terrestre:", vehiculo_terrestre)
print("Vehículo Aéreo:", vehiculo_aereo)
print("Vehículo Marítimo:", vehiculo_maritimo)
