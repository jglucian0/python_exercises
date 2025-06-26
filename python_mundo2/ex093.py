# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
partidas = []
jogador['nome'] = str(input("Inrisa o nome do jogador: "))
quat_partidas = int(input(f"Quantas partidas que {jogador['nome']} jogou? "))

for i in range(quat_partidas):
  gols_feitos = int(input(f"Quantos gols feitos na {i+1} partida: "))
  partidas.append(gols_feitos)
jogador['gols_total'] = sum(partidas)
jogador['lista_gols'] = partidas[:]

print('-=' * 30)
print(jogador)
print('-=' * 30)
for i, v in jogador.items():
  print(f"O campo {i} tem o valor {v}")
print('-=' * 30)
print(f"O jogador {jogador['nome']} jogou {quat_partidas} partidas")
for i, v in enumerate(jogador['lista_gols']):
  print(f"Na {i+1} partida fez {v} gols")
print(f"Foi um total e {jogador['gols_total']} gols")
print('-=' * 30)



