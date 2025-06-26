# Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
count_digitos = 0

for count in range(1, 501, 2):
  if count % 3 == 0:
    soma += count
    count_digitos += 1
print(f"A soma de {count_digitos} dígitos é igual a {soma}")