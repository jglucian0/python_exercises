# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

cheapest_product_price = None
cheapest_product_name = ""
products_above_1000 = 0
total_price = 0

while True:
  product_name = str(input("Nome do produto: "))
  product_value = float(input("Valor do produto: "))
  
  total_price += product_value
  
  if cheapest_product_price is None or cheapest_product_price > product_value:
    cheapest_product_price = product_value
    cheapest_product_name = product_name
  
  if product_value >= 1000:
    products_above_1000 += 1
    
  add_another_product = str(input("Deseja adicionar outro produto? [S/N] ")).upper()
  
  if add_another_product != "S":
        print(f"\nResumo da compra:")
        print(f"- Total gasto: R${total_price:.2f}")
        print(f"- Produtos acima de R$1000: {products_above_1000}")
        print(f"- Produto mais barato: {cheapest_product_name} por R${cheapest_product_price:.2f}")
        break
  
  

