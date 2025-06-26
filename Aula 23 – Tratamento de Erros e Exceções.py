# Nessa aula, vamos ver como o Python permite tratar erros e criar respostas a essas exceções. Aprenda como usar a estrutura try except no Python de uma forma simples.

# Tratamento de Erros com try / except

try:
    num = int(input("Digite um número: "))
    resultado = 10 / num
    print(f"Resultado: {resultado}")
except ValueError:
    print("Erro: você digitou um valor inválido. Digite um número inteiro.")
except ZeroDivisionError:
    print("Erro: divisão por zero não é permitida.")
except Exception as erro:
    print(f"Ocorreu um erro inesperado: {erro}")
else:
    print("Código executado com sucesso!")
finally:
    print("Fim do programa.")
