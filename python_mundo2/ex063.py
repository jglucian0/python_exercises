# Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
# Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

N = int(input("Insira um número inteiro qualquer: "))
F = [0, 1]
while len(F) < N:
  F.append(F[-1] + F[-2])
print(f"\nSequência de Fibonacci até o termo {N}")
print(F)

  


