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