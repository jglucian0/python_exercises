# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao_input = input("Insira uma expressão que utilize parênteses: ")
pilha = []

for caractere in expressao_input:
    if caractere == '(':
        pilha.append('(')  # Abre parêntese: empilha
    elif caractere == ')':
        if len(pilha) > 0:
            pilha.pop()  # Fecha parêntese: desempilha se houver algo
        else:
            pilha.append(')')  # Parêntese fechado sem abrir: erro
            break  # Já sabemos que está inválido

print(f"A expressão digitada foi: {expressao_input}")
if len(pilha) == 0:
    print("Esta expressão é válida!")
else:
    print("Erro, esta expressão é inválida! Verifique o fechamento dos parênteses...")

