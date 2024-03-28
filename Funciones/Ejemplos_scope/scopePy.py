"""
El scope o alcance de funciones y/o variables define a que van a poder acceder y a que no.
Variables definidas dentro de una funcion no se puede acceder desde afuera pero si por funciones que esten dentro de si.
Variables definidas fuera de funciones pueden ser referenciadas dentro de funciones
pero no modificadas a menos que se utilize el global para poder cambiar la referencia. (Es decir que la variable
dentro de la funcion apunte a la que esta fuera de)

Hay que pensarlo como si fuera una muneca rusa. Lo que esta adentro puede usar lo que esta afuera, pero lo que esta
afuera no lo que esta adentro.
"""

maxt = 100
opa = 5
print(maxt)


def print_max():
    global maxt   # Hace que la variable sea una referencia a la que esta afuera (es decir son la misma ahora)
    opa = 0
    maxt = maxt + 1
    print(maxt)
    print(opa)  # toma la definida en la funcion, no la externa


print_max()
print(opa)


def outer():
    title = 'original title'

    def inner():
        # nonlocal title   si pongo nonlocal title, toma como referencia a title la definida en la funcion externa.
        title = 'another title'
        print('inner:', title)
    inner()
    print('outer:', title)


outer()
