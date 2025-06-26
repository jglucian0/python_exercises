# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

lista_pessoas = []
pessoa = []
lista_peso_max = []
lista_peso_min = []
peso_max = peso_min = None

while True:
  pessoa.append(str(input("Insira o {}° nome: ")))
  pessoa.append(float(input("Insira seu peso: ")))
  lista_pessoas.append(pessoa[:])
  
  if peso_max is None or pessoa[1] > peso_max:
    peso_max = pessoa[1]
  if peso_min is None or pessoa[1] < peso_min:
    peso_min = pessoa[1]
    
  pessoa.clear()
  if str(input("Deseja continuar? [S/N] ")).strip().upper() != "S": break
  
for p in lista_pessoas:
  if p[1] == peso_max:
    lista_peso_max.append(p[0])
  if p[1] == peso_min:
    lista_peso_min.append(p[0])

print(f"Foram cadastradas um total de {len(lista_pessoas)} pessoas")
print(f"O maior peso registrado foi {peso_max}. De {lista_peso_max}")
print(f"O menor peso registrado foi {peso_min}. De {lista_peso_min}")