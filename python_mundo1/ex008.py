# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
user_input = float(input("Insira um valor para conversão: "))
print(
    "{}m convertido em centímetros é {:.0f}cm \n{}m convertido em milímetros é {:.0f}mm".format(
        user_input, user_input * 100, user_input, user_input * 1000
    )
)
