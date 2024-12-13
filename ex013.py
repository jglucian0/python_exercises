# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario = int(input("Digite o valor do seu saário: "))
aumento = (15 / 100) * salario
novo_salario = salario + aumento
print(f"O reajuste do seu salário com aumento de 15% é: {novo_salario:.2f}R$")
