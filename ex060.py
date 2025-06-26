# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

numero_escolhido = int(input("Insira um npumero para calcular seu fatorial: "))
fatorial = 1

print(f"Calculado... {numero_escolhido}! =", end=" ")
for i in range(numero_escolhido, 0, -1):
  fatorial = fatorial * i
  if i > 1:
    print(f"{i} x", end=" ")
  else:
    print(f"{i} =", end=" ")
print(fatorial)
