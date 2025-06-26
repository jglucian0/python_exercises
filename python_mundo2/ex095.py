# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

lista_jogadores = []

while True:
    jogador = {}
    partidas = []

    jogador['nome'] = input("Insira o nome do jogador: ").strip().capitalize()
    quant_partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

    for i in range(quant_partidas):
        partidas.append(int(input(f"Quantos gols fez na {i+1}° partida? ")))

    jogador['lista_gols'] = partidas[:]  # copia da lista
    jogador['gols_total'] = sum(partidas)

    lista_jogadores.append(jogador.copy())

    option_sair = input("Deseja adicionar outro jogador? [S/N] ").strip().upper()
    if option_sair != 'S':
        break

print('-=' * 30)
print(f"{'Cod':<5}{'Nome':<15}{'Gols':<20}{'Total':<10}")
print('-' * 50)

for k, v in enumerate(lista_jogadores):
    gols_str = str(v['lista_gols'])
    print(f"{k:<5}{v['nome']:<15}{gols_str:<20}{v['gols_total']:<10}")

print('-=' * 30)

while True:
    opcao_detalhes = int(input("\nDeseja mostrar detalhe de qual jogador? (999 para sair) "))
    if opcao_detalhes == 999:
        print("Finalizando...")
        break
    if 0 <= opcao_detalhes < len(lista_jogadores):
        jogador = lista_jogadores[opcao_detalhes]
        print('-=' * 30)
        print(f"Detalhes do jogador {jogador['nome']}:")
        for i, gols in enumerate(jogador['lista_gols']):
            print(f"  Na partida {i+1} fez {gols} gol(s)")
        print(f"Total de gols: {jogador['gols_total']}")
    else:
        print(f"ERRO! Não existe jogador com código {opcao_detalhes}. Tente novamente.")
