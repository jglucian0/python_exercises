# Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

# Tupla com os números por extenso
extenso = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco',
    'seis', 'sete', 'oito', 'nove', 'dez',
    'onze', 'doze', 'treze', 'quatorze', 'quinze',
    'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
)

user_number = int(input("Insira um número de 0 a 20: "))

if user_number >= 0 and user_number <= 20:
  print(extenso[user_number])
else:
  print("O número precisa estar entre 0 e 20")