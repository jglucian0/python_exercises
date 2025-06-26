# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
user_input = float(input("Insira qual valor possui na carteira: "))
value_dollar = 5.95
converted_amount = user_input / value_dollar
print(
    f"Com um saldo de {user_input:.2f}R$, você pode comprar {converted_amount:.2f}US$"
)
