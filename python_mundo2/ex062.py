# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

from time import sleep

primeiro_termo = int(input("Insira o primeiro termo: "))
razao = int(input("Insira a razão: "))
termo = primeiro_termo
count = 1
opcao_sair = False

while opcao_sair == False:
  while count <= 10:
    termo += razao
    
    if count == 10:
      print(termo, end= '.')
    else:
      print(termo, end= ', ')
    count += 1
    
  opcao_escolha = str(input("\nDeseja enviar mais algum termo? [S/N] ")).upper()
  if opcao_escolha == "S":
    sleep(1)
    print("\nEncerrando...")
    opcao_sair = True
  else:
    sleep(1)
    print("\nInforme os números novamente...")