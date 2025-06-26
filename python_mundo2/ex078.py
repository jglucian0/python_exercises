# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = list(int(input("Insira um número qualquer: ")) for _ in range(5))

valor_max = max(valores)
valor_min = min(valores)

print(f"A lista formada foi {valores}")
print(f"Encontrei o valor MAIOR {valor_max} na(s) posições(ão): ", end="")
for i, v in enumerate(valores):
  if v == valor_max:
    print(f"{i + 1}°", end=" ")


print(f"\nEncontrei o valor MENOR {valor_min} na(s) posições(ão): ", end="")
for i, v in enumerate(valores):
  if v == valor_min:
    print(f"{i + 1}°", end=" ")


