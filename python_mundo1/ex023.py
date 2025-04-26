# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

# Coletando o numero escolhido de 0 a 9999
numero = int(input("Digite um número: "))

# Realizando o fatiamento atrávez do método matematico, onde divido o numero pela numeraçao que desejo e tiro o módulo do resto da fração
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

# Imprimindo os resultados na formatação correta
print(
    f"\nUnidade: {unidade} \nDezena: {dezena} \nCentena: {centena} \nMilhar: {milhar}"
)
