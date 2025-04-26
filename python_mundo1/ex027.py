# Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

# Coletando a entradam de um nome
nome = str(input("Insira o seu nome completo: ")).strip()
nome_split = nome.split()

# Formatando a entrada e imprimindo o primeiro e ultimo nome
print("Seu primeiro nome é {}".format(nome_split[0]))
print("Seu último nome é {}".format(nome_split[len(nome_split) - 1]))
