"""
Ejercicio paso a paso :)

Un par de geeks van a hostear un juego de D&D digital y necesitan lo siguiente:
Un modelado para personas con raza (humano, elfo, enano), clase (guerrero, mago, arquero).
Un modelado para enemigos (lobos, orcos)
Un sistema que calcule la danio  [ # no tengo la enie, se escribir xD ]

Tanto las personas como los enemigos van a tener stats como HP (Hit points), AP (attack power) y XPL (experience lvl)
Las personas a la vez tienen MP.
Las clases y las razas alteran los valores de la HP, el AP y el MP.

Ambos enemigos y personas deben tener un metodo para atacar. Si la HP llega a 0 debe considerarse derrotado.
Ademas Quiero saber cuantas entidades (sin importar cual sea hay en el tablero tod el tiempo)

*Se debe realizar utilizando la menor cantidad de codigo posible*
    [Sugerencia, usar clases y herencia xD]
"""


""" Paso 1: Modelado de entidades de una clase 
    Me pregunto, que tienen en comun? Tiene sentido reciclar todo el codigo, o solo una parte?
    En base a eso me pongo a crear una clase llamda Entidad que tenga en comun lo de las personas y los enemigos.
    Ademas le agrego la variable de clase contador_de_entidades pues quiero saber cuantas hay todo el tiempo.
    
    Paso 2: 
    Pensar que metodos van a tener en comun las entidades. Atacar, calcular danio, morir, __str__
    En otras palabras si hay metodos que se pueden generalizar de forma que insertando x parametros pase una cosa
    u otra, se deberia poner eso directamente de forma que no haya que reescribir ese codigo 20 veces.
    
    Paso 3: 
    Implementacion. Conviene empezar por el padre para evitar confusiones sobre que van a tener de especifico los hijos
    o no.
    
    Paso 4: Una vez terminado el padre, seguir con los hijos, tratando de explotar todo lo que se implemento en el padre
    
    Paso 5: LLorar ah, chiste. Comprobar que no haya mas que tenga sentido reciclar o mandar a una clase padre.
"""


class Entidad:
    # Variables de clase que va a contar la cantidad de variables instanciadas
    contador_de_entidades = 0

    def __init__(self, hp, ap, xpl, raza):
        self.hp = self.__mod_hp(hp, raza, xpl)
        self.ap = ap
        self.xpl = xpl
        self.raza = raza
        Entidad.contador_de_entidades += 1

# el entity: 'Entidad' le aclara a python que estoy esperando que se pase una entidad ahi
    def attack(self, entity: 'Entidad'):
        entity.substract_hp(self.calculate_ap())
        print(f"Se realizo {self.calculate_ap()} de danio.")
        if entity.hp <= 0:
            entity.die()

    def substract_hp(self, dmg):
        self.hp -= dmg

    def calculate_ap(self):
        return self.ap + 0.5*self.xpl

    def die(self):
        Entidad.contador_de_entidades -= 1
        print(f"{self} ha muerto")

    def __str__(self):
        return f"Raza: {self.raza}, Nivel: {self.xpl}"

    @classmethod
    def modifier(cls, raza, stat):
        match raza:
            case "Human":
                return 0.75
            case "Elf":
                if stat == "mp":
                    return 1.3
                else:
                    return 1.1
            case "Dwarf":
                if stat == "mp":
                    return 0.4
                else:
                    return 1.5
            case "Wolf":
                return 0.9
            case "Orc":
                return 1.7

    @classmethod
    def __mod_hp(cls, hp, raza, xpl):
        return hp * cls.modifier(raza, hp) + 0.5 * xpl


class Person(Entidad):
    def __init__(self, hp, ap, xpl, mp, raza):
        super().__init__(hp, ap, xpl, raza)
        self.mp = self.mod_mp(mp, raza, xpl)

    @classmethod
    def mod_mp(cls, mp, raza, xpl):
        return mp * cls.modifier(raza, mp) + 0.5 * xpl

    def calculate_ap(self):
        return super().calculate_ap() + self.mp*0.75

    def __str__(self):
        return f"Persona, " + super().__str__()


class Enemy(Entidad):
    def __str__(self):
        return f"Enemigo, " + super().__str__()


"""
Como se puede ver, enemy y persona comparten MUCHISIMO, por lo que las clases enemy y person tienen muy pocas adiciones
y/o diferencias con entidad. Todo ese codigo se pudo reciclar gracias a eso.
"""
jugador1 = Person(100, 20, 1, 10, "Elf")
enemy1 = Enemy(100, 10, 3, "Wolf")

print(jugador1)
print(enemy1)
print(Entidad.contador_de_entidades)
jugador1.attack(enemy1)
print(enemy1.hp)
jugador1.attack(enemy1)
jugador1.attack(enemy1)
print(enemy1.hp)
jugador1.attack(enemy1)
print(Entidad.contador_de_entidades)
