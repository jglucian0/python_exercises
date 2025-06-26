# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

import random #Import library ramdom para sortear opção

opcoes = ["pedra", "papel", "tesoura"] #Define por meio de uma lista
escolha_maquina = random.choice(opcoes) #Utilzia o método choice para escolher uma opção da lista

# Escolha do jogador
print("\nVamos iniciar o Jokenpô!")
print("[1] - Pedra")
print("[2] - Papel")
print("[3] - Tesoura")
escolha_numero = int(input("\nEscolha uma das opções: "))

# Conversão de dígito para string
if escolha_numero == 1:
  escolha_jogador = "pedra"
elif escolha_numero == 2:
  escolha_jogador = "papel"
elif escolha_numero == 3:
  escolha_jogador = "tesoura"
else:
  print("Opção inválida!")
  exit()

# Lógica do jogo
if escolha_jogador == escolha_maquina:
  print("Empate")
elif (escolha_jogador == "pedra" and escolha_maquina == "tesoura") or \
     (escolha_jogador == "papel" and escolha_maquina == "pedra") or \
     (escolha_jogador == "tesoura" and escolha_maquina == "papel"):
       print("Jogador ganha")
elif (escolha_jogador == "pedra" and escolha_maquina == "papel") or \
     (escolha_jogador == "papel" and escolha_maquina == "tesoura") or \
     (escolha_jogador == "tesoura" and escolha_maquina == "pedra"):
       print("Maquina ganha")

print(f"Maquina escolheu: {escolha_maquina} | Jogador escolheu: {escolha_jogador}")