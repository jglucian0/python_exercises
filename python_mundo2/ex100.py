# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

import random

lst_numeros = []

def sort():
  for i in range(6):
    lst_numeros.append(random.randint(1, 10))
  print(f'Os 5 valores sorteados foram: {lst_numeros}')

def somPar():
  lst_numeros_par = []
  for n in lst_numeros:
    if n % 2 == 0:
      lst_numeros_par.append(n)
      sum_numeros_par = sum(lst_numeros_par)
  print(f'Somando os valores pares {lst_numeros_par} resulta em {sum_numeros_par}')
  
sort()
somPar()
    