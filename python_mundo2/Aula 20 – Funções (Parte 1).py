# Nessa aula, vamos aprender o que são funções ou rotinas e como utilizar funções em Python.
# Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python.
# Veja como funciona o comando def em Python e como utilizá-lo com parâmetros simples e múltiplos.

# funções nativas do python
# print(), len(), input(), int(), float()...

def linha():
  print('-' * 20)
  
linha()
print('SISTEMA DE ALUNOS')
linha()
print('CADASTRO DE FUNCIONÁRIO')
linha()

def mensagem(msg):
  print('-' * 20)
  print(msg)
  print('-' * 20)
  
mensagem('SISTEMA DE ALUNOS')

def soma(a, b):
  s = a + b
  print(s)
  
soma(4, 2)


# empacotamento de função
def soma(*valores):
  s = 0
  for num in valores:
    s += num
  print(s)

soma(4, 2)


def contador(*num):
  print(num)
contador(5, 7 ,3 , 1, 4)

def dobra(lst):
  pos = 0
  while pos < len(lst):
    lst[pos] *= 2
    pos += 1

valores = [7,2,3,4,1]
dobra(valores)
print(valores)
