# Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for count in range(1, 51):
  if count % 2 == 0:
    print(count)
    
for count in range(2, 51, 2): # Maneira mais adequada com menos interações
  print(count)