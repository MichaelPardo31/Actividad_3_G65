#Cree una clase Vehículo que contenga los atributos de instancia velocidad_maxima y kilometraje.

class Vehiculo:
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

mi_carro = Vehiculo("180", "44089")

print(mi_carro.velocidad_maxima, mi_carro.kilometraje)

