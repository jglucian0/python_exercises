# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

# Solicita um número inteiro para verificação
numero = int(input("Insira um número desejado: "))
is_primo = True # Defino o estado inicial como True

for i in range(2, numero): # Inicia o laço a partir do 2 até o número digitado
    if numero % i == 0: # Se o número foi divisível por qualquer número alem de 1 e 2 não sera primo
      is_primo = False
      break
    
if (numero < 2) or (is_primo == False):
  print(f"O número {numero} não é primo!")
else:
  print(f"O número {numero} é primo!")