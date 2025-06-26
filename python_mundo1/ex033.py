# Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

# Receber os três numeros digitados
n1 = int(input("Insira o primeiro númeiro: "))
n2 = int(input("Insira o segundo númeiro: "))
n3 = int(input("Insira o terceiro númeiro: "))

# Criar um fluxo onde valida qual é o maior e qual é o maior
maior = n1
menor = n1

if (n2 > maior):
  maior = n2
if (n3 > maior):
  maior = n3  

if (n2 < menor):
  menor = n2
if (n3 < menor):
  menor = n3

print(f"O maior número é: {maior}")
print(f"O menor númeiro é: {menor}")


# Determinar o maior e o menor usando funções nativas
# maior = max(n1, n2, n3)
# menor = min(n1, n2, n3)