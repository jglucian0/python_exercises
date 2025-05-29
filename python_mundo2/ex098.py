# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada


def contador(inicio, fim, passo):
  if passo < 0:
    passo *= -1
  if passo == 0:
    passo = 1
    
  print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
  print('-' * 50)
  
  if inicio < fim:
    count = inicio
    while count <= fim:
      print(f'{count} ', end='')
      count += passo
    print("FIM!")
  else:
    count = inicio
    while count >= fim:
      print(f'{count} ', end='')
      count -= passo
    print("FIM!")
    
print('-' * 50)
contador(0, 10, 1)
print('-' * 50)
contador(10, 0, 2)
print('-' * 50)
print('Sua vez, insira uma contagem personalizada: ')
inicio = int(input("\nInsira o valor de inicio: "))
fim = int(input("Insira o valor final: "))
passo = int(input("Insira o valor de passo: "))
print('-' * 50)
contador(inicio, fim, passo)
print('-' * 50)


