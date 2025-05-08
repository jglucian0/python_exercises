# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista d de forma e valores, ordenadadecrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista_numerica = []
count = 0

while True:
  lista_numerica.append(int(input("Insira um número qualquer: ")))
  count += 1
  
  if str(input("Deseja inserir outro número? [S/N] ")).strip().upper() != "S":
    break

lista_numerica.sort(reverse=True)
print(f"Foram digitados {count} números na lista.")
print(f"A lista formada foi {lista_numerica}")
if 5 in lista_numerica:
  print("O número 5 faz parte da lista.")
else:
  print("O número 5 não faz parte da lista.")