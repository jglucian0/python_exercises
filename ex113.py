# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.


def leiaInt(msg):
    while True:
        try:
            input_user = int(input(msg))
        except (ValueError, TypeError):
            print("Erro: você digitou um valor inválido. Digite um número inteiro.")
            continue
        except KeyboardInterrupt:
            print("Entrada de dados interrompido pelo usuário.")
            return 0
        else:
            return input_user


def leiaFloat(msg):
    while True:
        try:
            input_user = float(input(msg))
        except (ValueError, TypeError):
            print("Erro: você digitou um valor inválido. Digite um número tipo float.")
            continue
        except KeyboardInterrupt:
            print("Entrada de dados interrompido pelo usuário.")
            return 0
        else:
            return input_user


numA = leiaInt("Digite um número tipo inteiro: ")
numB = leiaFloat("Digite um número tipo float: ")
print(f"O valor inteiro digitado foi {numA}")
print(f"O valor real digitado foi {numB}")
