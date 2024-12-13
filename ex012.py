# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
valor_produto = float(input("Digite o valor do produto: "))
desconto = 5 / 100 * valor_produto
valor_descontado = valor_produto - desconto

print(f"O valor do produto com o desconto de 5% é: {valor_descontado:.2f}")
