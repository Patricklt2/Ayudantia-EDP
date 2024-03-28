
"""
Que es un string? 
Es una cadena caracteres o mas bien chars.
En python estas no son mutables. Es decir que una vez creadas asi quedan.
Hay distintas formas de trabajar y manipular strings.
Algunas formas son mas "rapidas" o eficientes para darles formato que otras.
"""

# Esta es una asignacion directa
nommi = "stella"


# El mas rapido de todos:
# f'blah blah {nombre_variable} blah blah'
# Es una funcion que esta muy optimizada (basicamente es mas rapida)
# Dentro de los corchetes van los nombres de las variables.
# Estos luego son reemplazados por el contenido de la variable en si

print(f'hola mundo {nommi}')

# El original y segundo mas rapido
# En vez de reemplazar en los corchetes, se reemplazan los %s
# la sintaxis '%s ....' % (variable o string, ...)

print('%s,%s' % (nommi, 'no'))

# Tercero mas rapido
# Reemplaza en los corchetes directamente, en el orden en el cual se encuentran las variables

format_string = "Welcome {}!"
print(format_string.format(nommi))

print(nommi)

# Hay caracteres especiales que se pueden poner dentro de los strings x ej:
print("\n \\ \t \b")

# \n inserta una linea nueva, \\ escribe la \, \t inserta un tab y \b es un backspace

""" En python son objetos. Entonces vienen con metodos de clase"""

# Aca hay algunos ejemplos

# ESTOS NO MODIFICAN EL STRING ORIGINAL. Retornan uno nuevo con los cambios
print(nommi.upper())
print(nommi.replace("ll", "oo"))

# Estos retornan verdadero o falso
print(nommi.__contains__("l"))
print(nommi.isalpha())
print(nommi.isnumeric())

# end
