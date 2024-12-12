# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor
input_user = int(input("Digite um número: "))
print(
    "Seu sucessor é: {}! \nSeu antecessor é: {}!".format(
        input_user + 1, input_user - 1
    ),
)
