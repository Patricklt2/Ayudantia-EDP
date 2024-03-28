"""
Un rey muy mala onda, tiene un hijo, el principe que ejerce su poder malevolamente. Los caballeros no estan de acuerdo
con las acciones, de ellos. Y clase media tampoco.

Cree un sistema de clases que incluya al rey, a su hijo, a los caballeros y la clase media.
El sistema debe cumplir lo siguiente:
1) Los caballeros deben poder atacar a otros. (Los caballeros, la clase media y la realeza deben portarse distinto al ser
atacados)
2) La clase media debe poder protestar. (hacer un metodo en el que protesten, [impriman a pantalla alguna queja])
3) El rey y el principe deben poder mandar gente a ser invitada a retirarse del reino. (Es decir que los saquen de la lista
4) Debe haber una lista de las personas que estan en el reino, en tod momento pues el rey tiene espias.


*Sugerencias para encarar esto*
A) Los objetos aca son todos personas por lo que se recomendaria hacer una clase persona
B) La lista tiene que poder ser consultada siempre.. podria ser una variable de clase persona
C) Se puede reciclar el comportamiento como reaccion a ser atacados en general y agregar luego lo unico de cada clase
en la misma clase

X ejemplo

clase persona:
    ....
    def reaccion(self):
    return f"AYYY exclama {self.name}"

    y luego en el rey x ejemplo

    def reaccion(self, agresor):
    self.chauchauadios(agresor)
    [lo invita a retirarse del reino *es decir lo saca de la lista en personas o whatever* ] (un tip es implementar un
    __eq__ para las personas.]
    return super().reaccion() + f"chau chau adios"
"""