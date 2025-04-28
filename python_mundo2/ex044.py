# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço normal 
# – 3x ou mais no cartão: 20% de juros

# Declara cada forma de pagamento e sua condição
DESCONTO_DINHEIRO = 0.90  # 10% de desconto
DESCONTO_CARTAO_1X = 0.95  # 5% de desconto
VALOR_NORMAL = 1.00        # Sem desconto
JUROS_CARTAO = 1.20        # 20% de juros

# Recebe a entrada do valor a ser pago
valor_produto = float(input("Insira o valor a ser pago no produto: "))
print("\n[1] - À vista dinheiro/cheque")
print("[2] - À vista no cartão")
print("[3] - Em até 2x no cartão")
print("[4] - Em até 10x no cartão")
condicao_pagamento = int(input("\nInsira o dígito correspondente a forma de pagamento: "))

if condicao_pagamento == 1:
  preco_final = valor_produto * DESCONTO_DINHEIRO
  print(f"Você recebeu 10% de desconto, o valor a ser pago é R${preco_final:.2f}")
elif condicao_pagamento == 2:
  preco_final = valor_produto * DESCONTO_CARTAO_1X
  print(f"Você recebeu 5% de desconto, o valor a ser pago é R${preco_final:.2f}")
elif condicao_pagamento == 3:
  preco_final = valor_produto * VALOR_NORMAL
  print(f"Você pagará o valor original de R${preco_final:.2f}")
elif condicao_pagamento == 4:
  preco_final = valor_produto * JUROS_CARTAO
  print(f"Você pagará juros da maquininha de 20%, valor a ser pago é R${preco_final:.2f}")
else:
  print("Você inseriu um dígito inválido!")