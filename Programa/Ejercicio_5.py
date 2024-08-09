# Cree una clase Circulo que tenga las propiedades centro y radio, las cuales se inicializan con parámetros en el constructor.
# Defina métodos en la clase para calcular el área,
# el perímetro e indicar si un punto pertenece al círculo o no.

import math

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def contiene_punto(self, punto):
        x1, y1 = self.centro
        x2, y2 = punto
        distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) # squrt es una funcion para encontrar raiz cuadrada
        return distancia <= self.radio

circulo = Circulo((0, 0), 5)

print(circulo.calcular_area())
print(circulo.calcular_perimetro())
print(circulo.contiene_punto((2, 3)))