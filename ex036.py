# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

# Recebendo os valores necessarios
valor_imovel = float(input("Insira o valor do imóvel: "))
salario = float(input("Insira seu salário líquido: "))
anos_pagamento = int(input("Em quantos anos o financiamento será quitado: "))

total_parcela = anos_pagamento * 12
valor_parcela = valor_imovel / total_parcela
limite_parcela = salario * 0.3

print(f"Valor da parcela: R$ {valor_parcela:.2f}")
print(f"Limite máximo da parcela (30% do salário): R$ {limite_parcela:.2f}")

if valor_parcela <= limite_parcela:
  print("Financiamento aprovado!")
  print(f"O imóvel de R$ {valor_imovel:.2f} será pago em {total_parcela}x de R$ {valor_parcela:.2f}")
else:
  print("Financiamento recusado!")
  print("O valor das parcelas excede 30% do seu salário.")
