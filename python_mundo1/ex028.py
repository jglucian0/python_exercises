# Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randrange
from time import sleep

# Gerando um número aleatório entre 0 e 5
print("-=-=-=-==-=-=-=-=-=-=-==-=-=-=-=-=-=-==-=-=-=-=-=-=-==-")
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=-=-=-==-=-=-=-=-=-=-==-=-=-=-=-=-=-==-=-=-=-=-=-=-==-")
numero_sorteado = randrange(6)


# Coletando o número escrolhido pelo usuário
numero_escolhido = int(input("Em qual número estou pensando? "))
print("Processando...")
sleep(0.5)

# Realizando a verificação e validação da resposta
if numero_escolhido == numero_sorteado:
    print("PARABENS! Você conseguiu acertar!")
else:
    print(f"ERROU! O número escolhido foi {numero_sorteado}")
