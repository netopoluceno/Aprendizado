#Aprendendo orientacao a objetos

"""
Objeto = instancia dentro da classe (quando criamos algo naquela classe)
Acessar algum valor: objeto.atributo
"""

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):       #Self = nome pra quem ta chamando, poderia ser outro nome
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

restaurante_praca = Restaurante('Praca', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

Restaurante.listar_restaurantes()

"""
Alguns metodos:
dir = mostra os metodos na classe
init = obriga passar parametros (construtor)
vars = mostra os valores do objeto
str = mostra o objeto em formato de texto
"""

"""classe é uma estrutura que encapsula dados e comportamentos relacionados. 
Além disso, os métodos em uma classe podem ser classificados em vários tipos com base em sua natureza e propósito."""

# ----------------------------

class Pessoa:
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome}, {self.idade} anos, {self.profissao}'

    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá, sou {self.nome}! Trabalho como {self.profissao}.'
        else:
            return f'Olá, sou {self.nome}!'

    def aniversario(self):
        self.idade += 1


# Criando 3 instâncias da classe Pessoa
pessoa1 = Pessoa(nome='Alice', idade=25, profissao='Engenheira')
pessoa2 = Pessoa(nome='Luiza', idade=30, profissao='Desenvolvedor')
pessoa3 = Pessoa(nome='Jaque', idade=22)

# Imprimindo informações iniciais
print("Informações Iniciais:")
print(pessoa1)
print(pessoa2)
print(pessoa3)
print()

# Utilizando o método de instância aniversario para aumentar a idade de uma pessoa
pessoa1.aniversario()
pessoa3.aniversario()

# Imprimindo informações após aniversário
print("Informações após aniversário:")
print(pessoa1)
print(pessoa3)
print()

# Utilizando o método de classe saudacao para exibir mensagens personalizadas
print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)


"""@property
modificar como um atributo é lido

self._atributo --- ._ = atributo protegido

@classmethod
indicar que aquela função é da classe
"""