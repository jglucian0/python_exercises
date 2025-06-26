# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
# Desafio 9 = # Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada

# Solicita ao usuário o número para gerar a tabuada
tabuada_escolhida = int(input("Digite o número para o qual deseja ver a tabuada: "))

# Loop de 0 até 10 para gerar a tabuada
for multiplicador in range(11):
  resultado = tabuada_escolhida * multiplicador
  print(f"{tabuada_escolhida} x {multiplicador} = {resultado}")