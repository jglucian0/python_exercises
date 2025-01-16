# Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO"

# Coletando o nome da cidade
cidade = str(input("Insira o nome de uma cidade: ")).strip()

# Realizando a formatação e filtrando a string "SANTO" para imprimir o resultado
print(cidade[:5].upper() == "SANTO")
