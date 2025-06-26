# Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

# Recebe o peso e a altura de uma pessoa
altura = float(input("Insira sua altura: ")) 
peso = float(input("Insira seu peso corporal: "))

# Realiza o calculo IMC
altura_ao_quadrado = altura * altura
indice_imc = peso / altura_ao_quadrado

# Baseado no seu IMC retona o status ao usuário
if indice_imc < 18.5:
  print(f"Seu IMC é {indice_imc:.2f} | Status: Abaixo do Peso")
elif indice_imc >= 18.5 and indice_imc < 25:
  print(f"Seu IMC é {indice_imc:.2f} | Status: Peso Ideal")
elif indice_imc >= 25 and indice_imc < 30:
  print(f"Seu IMC é {indice_imc:.2f} | Status: Sobrepeso")
elif indice_imc >= 30 and indice_imc < 40:
  print(f"Seu IMC é {indice_imc:.2f} | Status: Obesidade")
else:
  print(f"Seu IMC é {indice_imc:.2f} | Status: Obesidade Mórbida")
