# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista_numerica = []

for i in range(5):
  number_input = int(input("Insira um número qualquer: "))
  
  if not lista_numerica or number_input >= lista_numerica[-1]:
    lista_numerica.append(number_input)
  else:
    for i in range(len(lista_numerica)):
      if number_input <= lista_numerica[i]:
        lista_numerica.insert(i, number_input)
        break
    
print(lista_numerica)    
  
  

