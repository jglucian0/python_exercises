# Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

print("Contagem regressiva para o estouro dos fogos:")
sleep(0.5)
for count in range(10, 0, -1):
  print(count)
  sleep(0.5)
print("Estouro!")