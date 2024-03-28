"""
Funciones lambda, son escencialmente una forma de acortar la creacion de una funcion. Son bastante utiles pues ocupan
menos codigo y se pueden utilizar como valor de retorno. Lo que tiene aplicaciones interesantes.
"""

# apply es una funcion que toma como parametros una variable y un puntero a una funcion
# Y va a aplicar a la variable que se pase, la funcion pasada


def apply(x, function):
    result = function(x)
    return result


print(apply(2, lambda x: x + 2))


# Funcion que retorna una funcion lambda en base a que string se le pase


def make_checker(s):
    if s == 'even':
        return lambda n: n % 2 == 0
    elif s == 'positive':
        return lambda n: n >= 0
    elif s == 'negative':
        return lambda n: n < 0
    else:
        raise ValueError('Unknown request')


# Asi puedo crear multiples funciones con los distintos usos, sin que este definida o en memoria hasta que se
# tengan que usar.


f1 = make_checker('even')
f2 = make_checker('positive')
f3 = make_checker('negative')

print(f1(3))
print(f2(3))
print(f3(3))


def multiply(a, b):
    return a * b


# multby es una funcion que retorna funciones que multiplican numeros por un valor dado fijo.
# Combina funciones lambda y funciones definidas. (Otro ejemplo de uso)


def multby(func, num):
    return lambda y: func(num, y)


double = multby(multiply, 2)
triple = multby(multiply, 3)

print(double(5))
print(triple(5))

"""
Las funciones lambda tambien se usan para pasar como parametro para comparadores u organizadores. 
Seria como decirle a la compu que se tienen que organizar de forma que satisfagan las condiciones impuestas por la
lambda. Queda mas prolijo de esa forma.
"""

# end
