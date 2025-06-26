import moeda

preco = float(input("Digite o preço: R$"))
print(f'A metade de {preco}R$ é {moeda.metade(preco)}')
print(f'O dobro de {preco}R$ é {moeda.dobro(preco)}')
print(f'O aumento de 10% é {moeda.aumentar(preco, 10)}')
print(f'A subtração de 10% é {moeda.diminuir(preco, 10)}')