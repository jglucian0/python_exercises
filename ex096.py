# Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(l, c):
  a = c * l
  print(f"O terreno de {l}x{c} possue uma área de {a}m²")

print('-' * 50)
largura = float(input("Insira a largura do terreno (m): "))
comprimento = float(input("Insira o comprimento do terreno (m): "))
print('-' * 50)
area(largura, comprimento)
print('-' * 50)
