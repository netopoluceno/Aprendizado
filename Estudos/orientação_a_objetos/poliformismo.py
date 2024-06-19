class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        import math
        return math.pi * (self.raio ** 2)

# Função que aceita qualquer forma que tenha um método area
def imprimir_area(forma):
    print(f"A área é: {forma.area()}")

quadrado = Quadrado(4)
circulo = Circulo(3)

imprimir_area(quadrado)  # Saída: A área é: 16
imprimir_area(circulo)  # Saída: A área é: 28.274333882308138
