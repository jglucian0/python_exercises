# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

# Entrada do salário digitado
salario = float(input("Qual é o salário do funcionário: "))

#
if (salario <= 1250):
  salario_corrigido = salario + (salario * 0.15)
else:
  salario_corrigido = salario + (salario * 0.1)
  
  
print(f"O salario corrigido será: R${salario_corrigido:.2f}")
  