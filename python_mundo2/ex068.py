# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random
from time import sleep

calc_total = 0
count_number = 0

while True:
  machine_number = random.randrange(1, 11)
  number_user = int(input("Insira um número de 1 a 10: "))
  calc_total = machine_number + number_user
  option_user = str(input("Escolha PAR OU IMPAR [P/I] ")).upper()
    
  if calc_total % 2 == 0:
    if option_user == "P":
      count_number += 1
      print(f"\nO número foi {calc_total} e deu PAR")
      print("Você ganhou!")
      sleep(1)
      print("\nVamos jogar novamente!")
    elif option_user == "I":
      print(f"\nO número foi {calc_total} e deu PAR")
      print("Você perdeu!")
      break
    else:
      print("Escolha inválida... Encerrando.")
      break
  else:
    if option_user == "I":
      count_number += 1
      print(f"\nO número foi {calc_total} e deu IMPAR")
      print("Você ganhou!")
      sleep(1)
      print("\nVamos jogar novamente!")
    elif option_user == "P":
      print(f"\nO número foi {calc_total} e deu IMPAR")
      print("Você perdeu!")
      break
    else:
      print("\nEscolha inválida... Encerrando.")
      break

print(f"\nVocê teve {count_number} vitórias")    

      
    
  

  