# Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

from time import sleep

calc_multiplicacao = 0

while True:
  choice_number = int(input("Insira um número qualquer para formar a tabuada: "))
  
  if choice_number < 0:
    print("Encerrando...")
    sleep(1)
    break
  else:
    print(f"-== tabuada escolhida foi a do {choice_number} ==-")
    sleep(1)
    for i in range(11):
      calc_multiplicacao = choice_number * i
      print(f"{choice_number} x {i} = {calc_multiplicacao}")