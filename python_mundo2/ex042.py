# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

# Entrada dos comprimentos dos lados
ladoA = int(input("Informe o comprimento do lado A: "))
ladoB = int(input("Informe o comprimento do lado B: "))
ladoC = int(input("Informe o comprimento do lado C: "))

# Verifica se os lados formam um triângulo e qual categoria se enquadra
if (ladoA + ladoB > ladoC) and (ladoA + ladoC > ladoB) and (ladoB + ladoC > ladoA):
  if ladoA == ladoB and ladoB == ladoC:
    print("Equilatero")
  elif ladoA == ladoB  or ladoB == ladoC:
    print("Isosceles")
  elif ladoA != ladoB and ladoB != ladoC:
    print("Escaleno")
else:
  print("As medidas enviadas NÃO PODEM formar um triângulo.")
