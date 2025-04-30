# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = ""

while sexo != "M":
  sexo = str(input("Insira seu gênero (M/F): ")).upper().strip()
  
  if sexo == "M":
    print("O gênero escolhido foi Masculino")
  elif sexo == "F":
    print("O gênero escolhido foi Feminino")
  else:
    print("Dígito inválido! Escolha entre 'M' ou 'F'")
