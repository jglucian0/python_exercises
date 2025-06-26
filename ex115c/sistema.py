from .lib.interface import *
from .lib.arquivo import *

arquivo = 'C:/python_exercises/python_mundo2\ex115c/arquivo1.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(
        ['CADASTRAR NOVA PESSOA', 'LISTAR PESSOAS', 'SAIR DO SISTEMA'])
    if resposta == 1:
        header('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arquivo, nome, idade)
    elif resposta == 2:
        lerArquivo(arquivo)
    elif resposta == 3:
        print('Saindo do sistema... Até logo!')
        break
