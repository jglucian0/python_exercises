# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*num):
  cont = maior = 0
  print("Analisando os valores registrados...")
  
  for valor in num:
    if cont == 0 or valor > maior:
      maior = valor
    cont += 1
  
  print(f'\nForam informados {cont} valores...')
  print(f'O maior valor informado foi {maior}')

maior(3,2,5,4,9,10,7)
maior(4,3,5)
maior(6)
maior()