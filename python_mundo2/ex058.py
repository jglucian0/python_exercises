# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random
from time import sleep

numero_aleatorio = random.randrange(0, 11)
numero_escolhido = None
acertou = False
count_tentativas = 0

while acertou == False:
  numero_escolhido = int(input("\nInsira um número de 0 a 10: "))

  print("\nPensando...")
  sleep(1)
  if numero_aleatorio == numero_escolhido:
    print(f"\nParabéns, você acertou! Você teve {count_tentativas} palpites até acertar")
    acertou = True
    break
  elif numero_escolhido < numero_aleatorio:
    print("\nO número sorteado é MAIOR...")
    print("Infelizmente você errou! Tende novamente")
    count_tentativas += 1
  elif numero_escolhido < numero_aleatorio:
    print("\nO número sorteado é MENOR...")
    print("Infelizmente você errou! Tende novamente")
    count_tentativas += 1





# Realizar o ramdon de um numero de 0 a 10
# vai iniciar um looping solicitando o numero que acha que é o correto
# vai ser condicionado a Numero_random == numero_enviado para parar o programa