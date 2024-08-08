#Cree una clase Punto que represente un punto en el plano cartesiano.
# A la clase del punto anterior, defínale los siguientes métodos:
# - Un método mostrar que imprima por consola las coordenadas del punto
# - Un método mover que cambie las coordenadas del punto
# - Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto.
import math
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        

    def mostrar(self):
        print(f"posicion(en x, {self.x}/ en y, {self.y})")
    
    
    def mover(self):
        print(f"predeterminada posicion(en x, {self.x}/ en y, {self.y})")
        self.x = int(input("ingrese la posicion de x "))
        self.y = int(input("ingrese la posicion de y "))
        print(f"({self.x}, {self.y})")

    def calcular_distancia(self, punto_2):
        px = punto_2.x - self.x
        py = punto_2.y - self.y
        return math.sqrt(px**2 + py**2)

p1 = Punto(2,1)
p2 = Punto(3,5)
dist = p1.calcular_distancia(p2)
print(f"La distancia entre los puntos es: {dist:.2f}")