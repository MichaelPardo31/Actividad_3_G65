#aqui voy a hacer unas pruebas y ensayos de lo visto en clase, luego hago la actividad de clase

# class Naranja:
#     def __init__(self, color, sabor):
#         self.color = color
#         self.sabor = sabor

#     def crecer(self):
#         self.diametro = "6cm"


# mi_naranja = Naranja("Amarilloso", "dulce")

# print(mi_naranja.diametro)
# segunda_naranja = Naranja("opaca", "viejo")
# print(mi_naranja.sabor)

# siguiente clase dia 05 agosto

from datetime import datetime
class Gato:
    def __init__(self, tipo_pelo, raza, color, nombre, genero, peso):
        self.tipo_pelo = tipo_pelo
        self.raza = raza
        self.color = color
        self.nombre = nombre
        self.genero = genero
        self.edad = datetime.now()
        self.peso = peso
        self.nivel_de_energia = 100

#creacion de comportamientps (metodos)
## saltar
    def saltar(self):
        print(f"Hola soy {self.nombre} y estoy saltando en dos patas zunga")
#comer
#dormir
    def dormir(self, horas):
        print("Hola, antes de dormir tenía {} de energía".format(self.nivel_de_energia))

        if horas == 16:
            self.nivel_de_energia = 100
        elif horas == 8:
            self.nivel_de_energia += 40
        elif horas == 1:
            self.nivel_de_energia += 5

        # Asegurarse de que el nivel de energía no supere 100
        if self.nivel_de_energia > 100:
            self.nivel_de_energia = 100

        print("Hola, antes de dormir tenía {} de energía".format(self.nivel_de_energia))

#cumplir_anhios
#respirar
#caminar
#maullar

gato = Gato("poquito", "criollo", "multicolor", "Dalian", "hembra", "6kg")
#gato.saltar()
#print(gato.saltar)
print(gato.dormir(1))