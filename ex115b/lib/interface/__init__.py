# Exercício Python 115b: Vamos ver como fazer acesso a arquivos usando o Python.

def line(tam=42):
    return '-' * tam


def header(txt):
    print(line())
    print(txt.center(42))
    print(line())


def leiaInt(msg, lenlist):
    while True:
        try:
            n = int(input(msg))
            if n >= 1 and n <= lenlist:
                return n
        except (ValueError, TypeError):
            print(
                f'Opção inválida! Digite apenas um número entre 1 e {lenlist}.')
            continue
        except (KeyboardInterrupt):
            print(
                f'Opção inválida! Digite apenas um número entre 1 e {lenlist}.')
        else:
            print(
                f'Opção inválida! Digite apenas um número entre 1 e {lenlist}.')


def menu(list):
    header('MENU PRINCIPAL')
    c = 1
    for item in list:
        print(f'{c} - {item}')
        c += 1
    print(line())
    opc = leiaInt('Sua Opção: ', len(list))
    return opc
