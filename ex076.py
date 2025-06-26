# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

lista_produtos = (
    ('Melancia', 10.50),
    ('Banana', 20.75),
    ('Abóbora', 15.30),
    ('Maça', 9.99),
    ('Kiwi', 5.45)
)
print(f"{'Produto':<15} {'Preço':>6}")
print("-" * 22)
for (produto, preco) in lista_produtos:
    print(f"{produto:<14} R${preco:>5.2f}")