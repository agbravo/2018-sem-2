# Casino
from random import random

class Simulacion:

    def __init__(self, max_tiempo):
        self.max_tiempo = max_tiempo

    def llegar_nuevo_cliente(self):
        return random() <= 0.2

    def imprimir_estadistica(self, pozo):
        self.pozo = pozo      
        print('Dinero ganado (o perdido) por los clientes: ')
        print('Dinero ganado (o perdido) por los clientes por personalidad: ')
        print('Tiempo promedio de estadia en el casino')
        print('Tiempo promedio de estadia en el casino por personalidad')
        print('Ganancia del casino en promedio por dia: ')
        print('juego que genero la mayor ganancia en el casino: ')
        print('porcentaje de personas que conto cartas: ')
        print('razoes de salida del casino (%)')
        print('Tiempo total sin funcionar de cada instalacion')
        print('numero de personas que visito cada juego por dia')

    def funcionamiento_casino(self):
        pass
        
        
        
