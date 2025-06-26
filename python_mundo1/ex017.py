# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa
# Importando a biblioteca Math
from math import sqrt

# Entrada do comprimento do cateto oposto e adjacente
cateto_oposto = int(input("insira o comprimento do cateto oposto: "))
cateto_adjacente = int(input("Insira o comprimento do cateto adjacente: "))

# Realizando o calculo do comprimento da hipotenusa (c² = a² + b²)
valor_hipotenusa = sqrt((cateto_oposto**2) + (cateto_adjacente**2))

# Exibindo o resultado da hipotenusa
print(f"O comprimento da hipotenusa é: {valor_hipotenusa:.0f}")
