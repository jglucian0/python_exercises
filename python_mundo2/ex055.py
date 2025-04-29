# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior_peso = None
menor_peso = None

for i in range(1, 6):
  peso = float(input(f"Insira o peso da {i}° pessoa: "))

  if maior_peso is None or peso > maior_peso:
    maior_peso = peso
  elif menor_peso is None or peso < menor_peso:
    menor_peso = peso

print(f"O maior peso recebido foi {maior_peso} e o menor peso foi {menor_peso}")