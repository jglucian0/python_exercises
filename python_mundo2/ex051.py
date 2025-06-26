# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

# Solicita ao usuário o primero termo e a razão de uma PA
primeiro_termo = int(input("Insira o primeiro termo da sua PA: ")) 
razao = int(input("Insira a razão da sua PA: "))

for i in range(1,11):
  PA = primeiro_termo+(i-1)*razao
  print(PA, end= ', ')
  
print("Ababou!")