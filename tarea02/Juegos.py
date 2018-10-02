#Juegos
from abc import ABC
from random import randint

class Juegos(ABC):

    def __init__(self):
        self._probabilidad = None
        
    @property
    def probabilidad(self):
        return self._probabilidad

    @probabilidad.setter
    def probabilidad(self, valor):
        return sorted(0, valor, 1)[1]


class Tragamonedas(Juegos):

    def __init__(self, alfa):
        super().__init__(self)
        self.apuesta_min = 1
        self.probabilidad = alfa
        self.pozo = 0     #se vacia cuando la persona gana
        self.casino = 0

    def jugar(self, apuesta): #agregar alfa
        self.casino += 0.1 * apuesta
        self.pozo += 0.9 * apuesta 


class Ruleta(Juegos):

    def __init__(self, gama):
        super().__init__(self)
        self.var = gama
        self.probabilidad = None
        self.ganancia = 1
        self.casino = 0

    def jugar(self, apuesta): #agregar gama
        juego = randint(1, 4)
        if juego in (1, 4):
            self.probabilidad = 1 / (self.var + 1)
            self.ganancia = 5
        else:
            self.probabilidad = self.var / (2 * (self.var + 1))
            self.ganancia = 1.5
        
        
