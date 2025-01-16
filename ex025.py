# Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

# Coletando o nome de uma pessoa
nome = str(input("Insira o nome de uma pessoa: ")).strip()

# Realizando a formatação e filtrando a string "SILVA" para imprimir o resultado
print(f"Seu nome possui Silva? {"SILVA" in nome.upper()}")
