#DCCasino

from abc import ABC
from random import random, uniform, normalvariate, triangular
from random import randint
from parameters import alfa, beta, gamma
from parameters import teta, beta, gamma
from math import pi


class Persona(ABC):

    def __init__(self, rut, nombre, edad):
        self.nombre = nombre
        self.rut = rut
        self.edad = edad


class Cliente(Persona):

    def __init__(self, rut, nombre, edad, personalidad):
        super().__init__(rut, nombre, edad)
        self.personalidad = personalidad
        #self._dinero
        if self.personalidad == 'Ludopata':
            self._dinero = uniform(0.30, 0.69)
        elif self.personalidad == 'Kibitzer':
            self._dinero = uniform(0.00, 0.29)
        elif self.personalidad == 'Dieciochero':
            self._dinero = uniform(0.30, 0.69)
        elif self.personalidad == 'El ganador':
            self._dinero = uniform(0.30, 0.69)
        elif self.personalidad == 'Millonario':
            self._dinero = uniform(0.70, 1.00)
        #self._lucidez
        if self.personalidad == 'Ludopata':
            self._lucidez = uniform(0.30, 0.69)
        elif self.personalidad == 'Kibitzer':
            self._lucidez = uniform(0.30, 0.69)
        elif self.personalidad == 'Dieciochero':
            self._lucidez = uniform(0.00, 0.29)
        elif self.personalidad == 'El ganador':
            self._lucidez = uniform(0.30, 0.69)
        elif self.personalidad == 'Millonario':
            self._lucidez = uniform(0.30, 0.69)
        #self._ansiedad
        if self.personalidad == 'Ludopata':
            self._ansiedad = uniform(0.70, 1.00)
        elif self.personalidad == 'Kibitzer':
            self._ansiedad = uniform(0.00, 0.29)
        elif self.personalidad == 'Dieciochero':
            self._ansiedad = uniform(0.70, 1.00)
        elif self.personalidad == 'El ganador':
            self._ansiedad = uniform(0.30, 0.69)
        elif self.personalidad == 'Millonario':
            self._ansiedad = uniform(0.30, 0.69)
        #self._suerte
        if self.personalidad == 'Ludopata':
            self._suerte = uniform(0.30, 0.69)
        elif self.personalidad == 'Kibitzer':
            self._suerte = uniform(0.30, 0.69)
        elif self.personalidad == 'Dieciochero':
            self._suerte = uniform(0.30, 0.69)
        elif self.personalidad == 'El ganador':
            self._suerte = uniform(0.70, 1.00)
        elif self.personalidad == 'Millonario':
            self._suerte = uniform(0.30, 0.69)
        #self._sociabilidad
        if self.personalidad == 'Ludopata':
            self._sociabilidad = uniform(0.30, 0.69)
        elif self.personalidad == 'Kibitzer':
            self._sociabilidad = uniform(0.70, 1.00)
        elif self.personalidad == 'Dieciochero':
            self._sociabilidad = uniform(0.70, 1.00)
        elif self.personalidad == 'El ganador':
            self._sociabilidad = uniform(0.70, 1.00)
        elif self.personalidad == 'Millonario':
            self._sociabilidad = uniform(0.30, 0.69)
        #self._stamina
        if self.personalidad == 'Ludopata':
            self._stamina = uniform(0.70, 1.00)
        elif self.personalidad == 'Kibitzer':
            self._stamina = uniform(0.00, 0.29)
        elif self.personalidad == 'Dieciochero':
            self._stamina = uniform(0.30, 0.69)
        elif self.personalidad == 'El ganador':
            self._stamina = uniform(0.70, 1.00)
        elif self.personalidad == 'Millonario':
            self._stamina = uniform(0.70, 1.00)
        #self._deshonestidad
        if self.personalidad == 'Ludopata':
            self._deshonestidad = uniform(0.30, 0.69)
        elif self.personalidad == 'Kibitzer':
            self._deshonestidad = uniform(0.30, 0.69)
        elif self.personalidad == 'Dieciochero':
            self._deshonestidad = uniform(0.00, 0.29)
        elif self.personalidad == 'El ganador':
            self._deshonestidad = uniform(0.70, 1.00)
        elif self.personalidad == 'Millonario':
            self._deshonestidad = uniform(0.30, 0.69)
        self.dinero_entrada = self.dinero * 200
        self.ocupado = False

    @property
    def dinero(self):
        return self._dinero

    @dinero.setter
    def dinero(self, valor):
        return sorted(0, valor, 1)[1]

    @property
    def lucidez(self):
        return self._lucidez

    @lucidez.setter
    def lucidez(self, valor):
        return sorted(0, valor, 1)[1]

    @property
    def ansiedad(self):
        return self._ansiedad
            
    @ansiedad.setter
    def ansiedad(self, valor):
        return sorted(0, valor, 1)[1]

    @property
    def suerte(self):
        return self._suerte
            
    @suerte.setter
    def suerte(self, valor):
        return sorted(0, valor, 1)[1]

    @property
    def sociabilidad(self):
        return self._sociabilidad

    @sociabilidad.setter
    def sociabilidad(self, valor):
        return sorted(0, valor, 1)[1]
    
    @property
    def stamina(self):
        return self._stamina

    @stamina.setter
    def stamina(self, valor):
        return sorted(0, valor, 1)[1]

    @property
    def deshonestidad(self):
        return self._deshonestidad

    @deshonestidad.setter
    def deshonestidad(self, valor):
        return sorted(0, valor, 1)[1]

    def decisiones(self):
        numero = randint(1, 100)
        prob_retirarse = (1 - self.stamina)
        prob_jugar = min(self.ansiedad, 1 - prob_retirarse)
        prob_actividad = min(self.sociabilidad, 1 - prob_retirarse - prob_jugar)
        prob_instalacion  = 1 - (prob_retirarse + prob_jugar + prob_actividad) 
        if numero < (prob_retirarse * 100):
            return 'Retirarse'
        elif numero < (prob_jugar + prob_retirarse) * 100:
            #return 'Jugar'
            opcion = randint(1, 2)
            if opcion == 1:
                #return 'Tragamonedas'
                pass
            else:
                #return 'Ruleta'
                pass
        elif numero < (prob_jugar + prob_retirarse + prob_actividad) * 100:
            #return 'Actividad'
            duracion_actividad = max(self.lucidez + self.sociabilidad - self.ansiedad, 0.1) * pi ** 2
            opcion = randint(1, 3)
            if opcion == 1:
                #return 'conversar'
                pass
            elif opcion == 2:
                #return 'hablar con Tini'
                pass
            else:
                #return 'fisico determinista' 
                pass
        else:
            #return 'Instalacion'
            opcion = randint(1, 3)
            if opcion == 1:
                #return 'Restobar'
                pass
            elif opcion == 2:
                #return 'Tarot'
                pass
            else:
                #return 'Baño'
                pass


class Personal(Persona):

    def __init__(self, rut, nombre, edad, tipo):
        super().__init__(nombre, rut, edad)
        self.tipo = tipo
        #self.juego
        if self.tipo == 'Bartender':
            self.juego = 'Restobar'
        elif self.tipo == 'Dealer':
            self.juego = 'All'
        elif self.tipo == 'Mr. T':
            self.juego = 'Tarot'
        #self.tiempo
        if self.tipo == 'Bartender':
            self._tiempo = triangular(360, 540, 490)
        elif self.tipo == 'Dealer':
            self._tiempo = triangular(360, 540, 540)
        elif self.tipo == 'Mr. T':
            self._tiempo = triangular(360, 500, 420)
        self.turno_teminado = True
        self.descanso = None
        self.prox_turno = None

        @property
        def tiempo(self):
            return self._tiempo
        
        @tiempo.setter
        def tiempo(self, valor):
            return sorted(360, valor, 540)[1]

#-------------------------------------------------------------------------------
if __name__ == '__main__':
    vegeta = Cliente('345', 'Vegeta', 30, 'Millonario')
    Goku = Cliente('123', 'Goku', 30, 'Ludopata')
    Krilin = Cliente('124', 'Krilin', 34, 'Kibitzer')
