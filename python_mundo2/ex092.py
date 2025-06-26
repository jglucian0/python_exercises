from datetime import datetime
ano_atual = datetime.now().year

nome = input("Insira seu nome completo: ")
ano_nascimento = int(input("Insira seu ano de nascimento: "))
idade = ano_atual - ano_nascimento
ctps = int(input("Insira seu número da carteira de trabalho [0 - não possui]: "))

pessoa = {
    'nome': nome,
    'idade': idade,
    'ctps': ctps
}

if ctps != 0:
    ano_contratacao = int(input("Insira o ano de admissão: "))
    salario = float(input("Insira o valor do seu salário: "))
    tempo_contribuicao = ano_atual - ano_contratacao

    idade_aposentadoria = idade + max(0, 20 - tempo_contribuicao)

    pessoa['contratação'] = ano_contratacao
    pessoa['salário'] = salario
    pessoa['aposentadoria'] = idade_aposentadoria

print("\nDADOS CADASTRADOS:")
for chave, valor in pessoa.items():
    print(f"{chave} tem o valor {valor}")
