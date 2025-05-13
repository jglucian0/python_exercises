# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista
# única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista_numerica = [[], []]

for i in range(8):
  input_number = int(input("Insira um número qualquer: "))
  
  if input_number % 2 == 0:
    lista_numerica[0].append(input_number)
  else:
    lista_numerica[1].append(input_number)

lista_numerica[0].sort()
lista_numerica[1].sort()

print(f"Lista PAR em ordem crescente: {lista_numerica[0]}")  
print(f"Lista IMPAR em ordem crescente: {lista_numerica[1]}")
  
  