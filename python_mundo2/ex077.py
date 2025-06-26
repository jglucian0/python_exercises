# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('computador', 'programacao', 'python', 'desenvolvimento', 'algoritmo')

for p in palavras:
  print(f"\nAs vogais em '{p}' são  >  ", end="")
  for letra in p:
    if letra in 'aeiou':
      print(f"{letra}", end=" ")