# Nessa aula, vamos continuar a estudar os laços e vamos aprender a usar a estrutura de repetição while no Python. Por exemplo:
# c=1 while c !=10:
# print(c)
# c+=1
# print(‘Acabou’)

# Estrutura de repetição com teste lógico
has_coin = False
has_floor = False

while has_coin == True:
  print("Get a coin")
print("Walking")

while has_coin == False:
  if has_floor == True:
    print("Walking")
  elif has_floor == False:
    print("Jumping")
print("Get a coin")