# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele
user_input = input("Digite algo: ")

print(
    "Seu tipo primitivo é: {}! \nO valor do campo é alfanumérico? {}! \nO campo pertence à tabela ASCII? {}! \nO campo é decimal? {}! \nO valor do campo são dígitos? {}! \nO campo é um identificador válido? {}! \nO campo está em letras minúsculas? {}! \nO campo é numérico? {}! \nO campo é imprimível? {}! \nO campo está em branco? {}! \nO campo está em formato de título? {}! \nO campo está em letras maiúsculas? {}! \n".format(
        type(user_input),
        user_input.isalnum(),
        user_input.isascii(),
        user_input.isdecimal(),
        user_input.isdigit(),
        user_input.isidentifier(),
        user_input.islower(),
        user_input.isnumeric(),
        user_input.isprintable(),
        user_input.isspace(),
        user_input.istitle(),
        user_input.isupper(),
    )
)
