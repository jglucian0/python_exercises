# Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

# Entrada dos comprimentos dos lados
ladoA = int(input("Informe o comprimento do lado A: "))
ladoB = int(input("Informe o comprimento do lado B: "))
ladoC = int(input("Informe o comprimento do lado C: "))

# Verifica se os lados formam um triângulo
if (ladoA + ladoB > ladoC) and (ladoA + ladoC > ladoB) and (ladoB + ladoC > ladoA):
    print("As medidas enviadas PODEM formar um triângulo!")
else:
    print("As medidas enviadas NÃO PODEM formar um triângulo.")
    
valor = 3 * 5 + 4 ** 2
print(valor)