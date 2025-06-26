# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista_valores = []

while True:
  number_input = int(input("Insira um número qualquer: "))
  if number_input in lista_valores:
    print("O numero já existe! Não será adicionado.")
  else:
    lista_valores.append(number_input)
    
  option_exit = str(input("Deseja inserir outro número? [S/N]")).strip().upper()
  if option_exit != 'S':
    break
  
lista_valores.sort() 
print(f"A lista formada com números únicos foram: {lista_valores}")