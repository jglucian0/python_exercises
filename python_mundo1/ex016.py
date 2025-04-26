# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira
# Importação da biblioteca Math
from math import trunc

# Entrada de um número real
numero_real = float(input("Digite um número Real qualquer: "))

# Extraindo a parte inteira
parte_inteira = trunc(numero_real)

# Exibindo o resultado
print(f"A parte inteira de {numero_real} é: {parte_inteira}")
