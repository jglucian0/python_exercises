from .lib.interface import *

while True:
  resposta = menu(['CADASTRAR NOVA PESSOA', 'LISTAR PESSOAS', 'SAIR DO SISTEMA'])
  if resposta == 1:
    print('Opção 1')
  elif resposta == 2:
    print('Opção 2')
  elif resposta == 3:
    print('Saindo do sistema... Até logo!')
    break