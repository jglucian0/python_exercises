# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import datetime
data_atual = datetime.now().year

count_maioridade = 0
count_menoridade = 0

# Solicito a data de nascimento de 7 pessoas
for i in range (1,8):
  data_nascimento = int(input(f"Insira a data de nascimento da {i}° pessoa: "))
  idade = data_atual - data_nascimento
  if idade >= 18:
    count_maioridade += 1
  else:
    count_menoridade += 1

if count_menoridade == 0:
  print(f"Todas as {count_maioridade} pessoas já atingiuaram a maioridade.")
else:
  print(f"{count_maioridade} pessoa(s) já atingiu(aram) a maioridade, enquanto {count_menoridade} ainda são menores de idade.")

