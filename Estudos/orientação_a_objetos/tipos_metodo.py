class Pessoa:
    contador = 0

    def __init__(self, nome):
        self.nome = nome
        Pessoa.contador += 1

    @classmethod
    def contar_pessoas(cls):
        return f"Existem {cls.contador} pessoas."

    @staticmethod
    def boas_vindas():
        return "Bem-vindo(a)!"

# Criando instâncias da classe Pessoa
pessoa1 = Pessoa("Alice")
pessoa2 = Pessoa("Bob")

print(Pessoa.contar_pessoas())  # Saída: Existem 2 pessoas.
print(Pessoa.boas_vindas())  # Saída: Bem-vindo(a)!
