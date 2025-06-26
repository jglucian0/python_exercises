# Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

count_numbers = 0
calc_total = 0

while True:
  user_number = int(input("Insira um número qualquer: "))
  if user_number == 999:
    print(f"Você digitou {count_numbers} números e a soma entre eles foi {calc_total}")
    break
  else:
    count_numbers += 1
    calc_total += user_number