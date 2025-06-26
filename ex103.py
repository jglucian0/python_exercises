# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome, gols):
  print('-=' * 25)
  print(f'O jogador {nome} marcou {gols} gol(s).')
  print('-=' * 25)

nome_jogador = str(input("Insira o nome do jogador: ")).strip().capitalize()
gols = str(input("Insira quantos gols o jogador fez: "))
if gols.isnumeric():
  gols = int(gols)
else:
  gols = 0
if nome_jogador == '': nome_jogador = '<desconhecido>'
ficha(nome_jogador, gols)