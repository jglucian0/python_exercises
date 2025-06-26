# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[], [], []]
matriz_soma_pares = 0
soma_terceira_coluna = 0
maior_segunda_linha = 0

for linha in range(3):
  for coluna in range(3):
    matriz[linha].append(int(input(f"Digite um número para [{linha}, {coluna}]")))
  soma_terceira_coluna += matriz[linha][2]
    
for linha in matriz:
  for valor in linha:
    print(f"[ {valor:^3} ]", end="")
    if valor % 2 == 0:
      matriz_soma_pares += valor
  print()
maior_segunda_linha = max(matriz[1])

print(f"A soma total dos valores pares da matriz é: {matriz_soma_pares}")
print(f"A soma da terceira coluna é: {soma_terceira_coluna}")
print(f"O maior valor da segunda linha é: {maior_segunda_linha}")