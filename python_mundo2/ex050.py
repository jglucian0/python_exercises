# Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

# Solicita ao usuário 6 dígitos inteiros e realiza a soma apenas dos PARES
soma = 0
count_numeros = 0
for i in range(6):
  numero = int(input("Insira um dígito: "))
  if numero % 2 == 0:
       soma += numero
       count_numeros += 1
print(f"A soma entre os {count_numeros} números pares é {soma}")
