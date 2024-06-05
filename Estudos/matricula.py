#CRIAR UMA MATRÍCULA PARA UM ALUNO

from random import randint

estudantes = ["João", "Maria", "José", "Cláudia", "Ana"]

def gera_codigo():
  return str(randint(0,999))

codigo_estudantes = []

#Matrícula aleatória:
for i in range(len(estudantes)): 
  codigo_estudantes.append((estudantes[i], gera_codigo()))

#Matrícula com inicial do nome:
#for i in range(len(estudantes)): 
#  codigo_estudantes.append((estudantes[i], estudantes[i][0] + gera_codigo()))

codigo_estudantes