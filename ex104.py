# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
# ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(X):
  while True:
    input_user = input(X)
    if input_user.isnumeric():
      print(f'Valor {input_user} aceito, é um valor numérico.')
      break
    else:
      print('Valor não aceito, digite apenas valores numéricos!')

leiaInt('Digite um número: ')
  