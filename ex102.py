# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e
# outro chama o show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

numero = int(input("Digite um número para calcular o fatorial: "))

def fatorial(x, show=False):
  f = 1
  for c in range(x, 0, -1):
    if show:
      print(c, end='')
      if c>1:
        print(f' x ', end='')
      else:
        print(' = ', end='')
    f *= c
  return f

print(fatorial(5))
print(fatorial(5, show=True))