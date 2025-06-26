from .lib.interface import *
from .lib.arquivo import *

arquivo = 'C:/python_exercises/python_mundo2/ex115b/arquivo.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(
        ['CADASTRAR NOVA PESSOA', 'LISTAR PESSOAS', 'SAIR DO SISTEMA'])
    if resposta == 1:
        print('Opção 1')
    elif resposta == 2:
        lerArquivo(arquivo)
    elif resposta == 3:
        print('Saindo do sistema... Até logo!')
        break
