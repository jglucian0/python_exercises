# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada
input_user = int(input("Insira um número para gerar sua tabuada: "))

# Método simples porém complicado
print("Método sem utilizar For")
print(
    "{} x 1 = {} \n{} x 2 = {} \n{} x 3 = {} \n{} x 4 = {} \n{} x 5 = {} \n{} x 6 = {} \n{} x 7 = {} \n{} x 8 = {} \n{} x 9 = {} \n{} x 10 = {}".format(
        input_user,
        input_user * 1,
        input_user,
        input_user * 2,
        input_user,
        input_user * 3,
        input_user,
        input_user * 4,
        input_user,
        input_user * 5,
        input_user,
        input_user * 6,
        input_user,
        input_user * 7,
        input_user,
        input_user * 8,
        input_user,
        input_user * 9,
        input_user,
        input_user * 10,
    )
)

# Método mais adequado e legível utilizando For
print("\nMétodo utilizando For")
for i in range(1, 11):
    print(f"{input_user} x {i} = {input_user * i}")
