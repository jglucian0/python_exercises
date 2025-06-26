# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matriz = [[], [], []]

for linha in range(3):
  for coluna in range(3):
    matriz[linha].append(int(input(f"Digite um valor para [{linha}, {coluna}] ")))
  
print("\nMatriz formatada:")
for linha in matriz:
  for valor in linha:
    print(f'[ {valor:^3} ]', end='')
  print()
  