# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
# quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados

# Entrada de dados
largura = float(input("Quantos metros de largura possui a parede? "))
altura = float(input("E quantos metros de altura ela possui? "))

# Cálculo da área
area = largura * altura

# Considerando que 1 litro de tinta cobre 2 metros quadrados
litros_necessarios = area / 2

print(
    f"Para pintar uma parede de {area:.1f}m² será necessário {litros_necessarios:.1f}l de tinta"
)
