# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

# Recebe a entrada de dois números inteiros
n1 = int(input("Insira o primeiro número inteiro: "))
n2 = int(input("Insira o segundo número inteiro: "))

# Reliza uma condição de 3 verificações para emitir uma mensagem
if n1 == n2:
  print(f"Os dois números são IGUAIS") 
elif n1 > n2:
  print(f"O número {n1} é MAIOR que o númeiro {n2}") 
else:
  print(f"O número {n1} é MENOR que o númeiro {n2}") 
