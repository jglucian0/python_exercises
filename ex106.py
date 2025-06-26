# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

def ajuda(comando):
    print('\033[44m', end='')  # Fundo azul
    print(f"Acessando o manual do comando '{comando}'")
    print('\033[m', end='')  # Reset da cor
    print('\033[7m')  # Texto invertido (fundo branco)
    help(comando)
    print('\033[m')  # Reset

def titulo(msg, cor=42):
    print(f'\033[{cor}m{"~" * (len(msg) + 4)}')
    print(f'  {msg}')
    print(f'{"~" * (len(msg) + 4)}\033[m')

def sistema():
    while True:
        titulo('SISTEMA DE AJUDA PyHelp', 42)  # Verde
        comando = input('Função ou Biblioteca > ')
        if comando.upper() == 'FIM':
            titulo('ATÉ LOGO!', 41)  # Vermelho
            break
        else:
            ajuda(comando)

sistema()
