# Cree una clase Rectángulo la cual contiene dos atributos de instancia que representan los puntos que definen sus esquinas.
# Agregue métodos a la clase Rectángulo para calcular su perímetro,
# calcular su área e indicar si el rectángulo es un cuadrado.

class Rectangulo:
    def __init__(self, esquinaA, esquinaB):
        self.esquinaA = esquinaA 
        self.esquinaB = esquinaB

    def calcular_perimetro(self):
        ancho = abs(self.esquinaB[0] - self.esquinaA[0])
        alto = abs(self.esquinaB[1] - self.esquinaA[1])
        return 2 * (ancho + alto)

    def calcular_area(self):
        ancho = abs(self.esquinaB[0] - self.esquinaA[0])
        alto = abs(self.esquinaB[1] - self.esquinaA[1])
        return ancho * alto

    def cuadrado(self):
        ancho = abs(self.esquinaB[0] - self.esquinaA[0])
        alto = abs(self.esquinaB[1] - self.esquinaA[1])
        return ancho == alto

objeto = Rectangulo((7, 5), (7, 55))

print(objeto.calcular_perimetro())
print(objeto.calcular_area())
print(objeto.cuadrado())


