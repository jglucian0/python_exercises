# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
# APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

# Receber a entrada de uma frase qualquer
frase = str(input("Escreva uma frase qualquer: ")).upper().replace(" ","") # Formatting for capital letters and removing spaces
frase_invertida = frase[::-1] # Utilizo [::-1] para inverter a frase

if frase == frase_invertida: # Verifico se a frase normal e invertida são iguais para validação
  print(f"A frase {frase} é um palíndromo")
else:
  print(f"A frase {frase} não é um palíndromo")