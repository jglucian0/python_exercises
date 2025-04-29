# Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o “for”, que é uma estrutura versátil e simples de entender. Por exemplo:
# for c in range(0, 4):
# print(c)
# print(‘Acabou’)

# Estrutura de laço com variável de controle
for cont in range(0, 3): # Realiza a contagem 3x "count" pode mudar, serve para indentificação
  print("passo")
print("final")

# Estrutura de laço aninhada com estrutura de condição if
has_coin = True
for cont in range(0,3):
  if has_coin == True:
    print("pega")
  print("passo")
  print("pula")
print("final")