# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter
# apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista_numerica = []
lista_numerica_par = []
lista_numerica_impar = []

while True:
  number_input = int(input("Insira um número qualquer: "))
  lista_numerica.append(number_input)

  if str(input("Deseja inserir outro número? [S/N] ")).upper().strip() != "S": break

for indice, valor in enumerate(lista_numerica):
  if valor % 2 == 0:
    lista_numerica_par.append(valor)
  else:
    lista_numerica_impar.append(valor)
    
lista_numerica.sort()
lista_numerica_par.sort()
lista_numerica_impar.sort()

print(f"A lista formada foi {lista_numerica}")
print(f"Agora apenas com valores IMPAR {lista_numerica_impar}")
print(f"Agora apenas com valores PAR {lista_numerica_par}")
    