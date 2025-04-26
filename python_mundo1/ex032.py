# Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import datetime

# Coletando a entrada do ano digitado
ano = int(input("Digite o ano: "))

if ano == 0:
  ano = datetime.now().year

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
  print(f"{ano} é SIM um ano bissexto!")
else: 
  print(f"{ano} NÃO é um ano bissexto!")
