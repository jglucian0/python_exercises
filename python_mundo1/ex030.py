# Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

# Recebendo o numero inteiro digitado
number = int(input("Digite qualquer número inteiro: "))

# Realiza a verificação, onde todo número divisivel por 2 será PAR, caso contrário será IMPAR
if number % 2 == 0:
  print(f"O número {number} é PAR")
else:
  print(f"O número {number} é IMPAR")