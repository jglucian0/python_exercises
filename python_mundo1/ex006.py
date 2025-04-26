# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
input_user = int(input("Digite um número: "))

print(
    "O dobro do seu valor é: {}! \nO triplo do seu valor é: {}! \nA raiza quadrada do seu valor é: {:.3}!".format(
        input_user * 2, input_user * 3, input_user ** (1 / 2)
    )
)
