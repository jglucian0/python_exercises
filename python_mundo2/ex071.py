# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado
# (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print("\n--- Caixa Eletrônico ---")
withdraw_amount = int(input("\nDigite o valor que deseja sacar: "))
bill = 100

print("\nVocê irá receber as seguintes cédulas: ")
while withdraw_amount != 0:
  bill_count = withdraw_amount // bill
  withdraw_amount -= bill * bill_count
  
  if bill_count != 0:
    print(f"{bill_count} notas de {bill}R$")
  
  if bill == 100:
    bill = 50
  elif bill == 50:
    bill = 20 
  elif bill == 20:
    bill = 10
  elif bill == 10:
    bill = 5
  elif bill == 5:
    bill = 1



