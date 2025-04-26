# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça
# para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

# Recebendo o número escolhido
numero = int(input("Insira o númeiro desejado: "))

# Envia uma lista de opções para o usuário e um input de escolha
print("\n[1] converter para Binário")
print("[2] converter para Octal")
print("[3] converter para Hexadecimal")
escolha = int(input("\nEscolha uma das opções de conversão: "))

# Realiza a filtragem baseado na opção escolhida para realizar a conversão
if escolha == 1:
  binario = bin(numero)[2:]
  print(f"O número {numero} em binário é {binario}")
elif escolha == 2:
  octal = oct(numero)[2:]
  print(f"O número {numero} em octal é {octal}")
else:
  hexadecimal = hex(numero)[2:].upper()
  print(f"O número {numero} em hexadecimal é {hexadecimal}")