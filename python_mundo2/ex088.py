# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint

lista_jogos = []

quantidade = int(input("Insira a quantidade de jogos a serem gerados: "))

for i in range(quantidade):
  lista_atual = []
  
  while len(lista_atual) < 6:
    num_aleatorio = randint(1, 60)
    if num_aleatorio not in lista_atual:
      lista_atual.append(num_aleatorio)
  
  lista_jogos.append(lista_atual[:])

print(lista_jogos)
for i, jogo in enumerate(lista_jogos):
  print(f"Jogo {i+1}°: {jogo}")


