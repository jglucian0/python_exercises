import moeda

preco = float(input("Digite o preço: "))
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'O aumento de 10% é {moeda.moeda(moeda.aumentar(preco, 10))}')
print(f'A subtração de 10% é {moeda.moeda(moeda.diminuir(preco, 10))}')