class Animal:
    def __init__(self, nome):
        self.nome = nome

    def mover(self):
        return f"{self.nome} está se movendo"

class Passaro(Animal):
    def mover(self):
        return f"{self.nome} está voando"

# Criando instâncias das classes
animal = Animal("Animal Genérico")
passaro = Passaro("Papagaio")

print(animal.mover())  # Saída: Animal Genérico está se movendo
print(passaro.mover())  # Saída: Papagaio está voando
