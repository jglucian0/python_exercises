# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

opcao_sair = False

while opcao_sair == False:
  valor_n1 = int(input("\nInsira o valor do primeiro dígito: ")) 
  valor_n2 = int(input("Insira o valor do segundo dígito: "))
  
  print("\nQual operação deseja realizar?")
  print("\n[ 1 ] somar")
  print("[ 2 ] multiplicar")
  print("[ 3 ] maior")
  print("[ 4 ] novos números")
  print("[ 5 ] sair do programa")
  escolha = int(input("\nInsira o dígito correspondente [X]: "))
  
  if escolha == 1:
    soma = valor_n1 + valor_n2
    print("\nCalculando...")
    sleep(1)
    print(f"\nO resultado da SOMA é {soma}")
  elif escolha == 2:
    multiplicacao = valor_n1 * valor_n2
    print("\nCalculando...")
    sleep(1)
    print(f"\nO resultado da MULTIPLICAÇÃO é {multiplicacao}")
  elif escolha == 3:
    print("\nVerificando...")
    sleep(1)
    if valor_n1 > valor_n2:
      print(f"\nO valor MAIOR é {valor_n1}")
    elif valor_n1 < valor_n2:
      print(f"\nO valor MAIOR é {valor_n2}")
    else:
      print(f"\nNão existe valor maior, os dois são iguais")
      
  elif escolha == 4:
    sleep(1)
    print("\nInforme os números novamente...")
  elif escolha == 5:
    print("\nEncerrando programa...")
    sleep(1)
    opcao_sair = True
  else:
    print("\nOpção inválida!")
  