#instalaciones
from abc import ABC
from random import normalvariant

class Instalacion(ABC):

    def __init__(self, identificador, ubicacion, nombre):
        self.identificador = identificador
        self.ubicacion = ubicacion
        self.nombre = nombre
        self.duracion_persona = None
        self.gente_espera = None
        self.capacidad_max = None
        self.costo = None
        self.personal = None
        self.funcionando = None


class Restobar(Instalacion):
       #bebidas
       #disminuyen 0.2  lucidez
       #disminuyen 0.15 ansiedad
       #disminuyen 0.3  posibilidad que se retiren del casino

       #si lucidez > ansiedad comprara una bebida
       #si lucidez < ansiedad comprara una comida
       #si lucidez = ansiedad eleccion aleatoria

       def __init__(self, identificador, ubicacion, nombre):
           super().__init__(identificador, ubicacion, nombre)
           #self.duracion_persona = ???
           self.capacidad_max = 20 #personas
           self.costo = 2 #por persona
           self.personal = 2 #bartenders


class Tarot(Instalacion):

       #puede aumentar la posibilidad de irse o aumentar la suerte

       def __init__(self, identificador, ubicacion, nombre):
           super().__init__(identificador, ubicacion, nombre)
           self.duracion_persona = normalvariant(3, 5) #minutos
           self.capacidad_max = 1 #persona
           self.costo = 10 #por persona
           self.personal = 1 #mr t (exacto)


class Bano(Instalacion):

       #disminucion 0.1 ansiedad

       def __init__(self, identificador, ubicacion, nombre):
           super().__init__(identificador, ubicacion, nombre)
           self.duracion_persona = normalvariant(3 * (1 - lucidez), 2) #minutos
           self.capacidad_max = 20 #persona
           self.costo = 0.2 #por persona
           self.personal = 0 

