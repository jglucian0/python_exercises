# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

# Coletando o nome completo e armazenando em uma variável string
nome_completo = str(input("Insira o seu nome completo: ")).strip()

# Formatando o nome para Lower Case e Upper Case
nome_completo_upper = nome_completo.upper()
nome_completo_lower = nome_completo.lower()

# Removendo os espaços e contando quantas strings possuem
nome_completo_strings = len(nome_completo) - nome_completo.count(" ")

# Utilizando o find para encontrar o primeiro espaço vazio e contar apenas o primeiro nome
primeiro_nome_strings = nome_completo.find(" ")

# Imprimindo resultados
print(
    f'Formatação do nome "{nome_completo}" \nUpper Case: {nome_completo_upper} \nLower Case: {nome_completo_lower} \nQuantidade total de strings: {nome_completo_strings} \nQuantidade de strings no primero nome: {primeiro_nome_strings}'
)
