# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import datetime

# Recebe a entrada da data de nascimento (ano)
ano_autal = datetime.now().year
ano_nascimento = int(input("Insira sua data de nascimento: "))

# Realiza a verificação de idade e retorna a resposta baseado na idade
idade = ano_autal - ano_nascimento

if idade == 18:
  print("Você completou 18 anos, deverá realizar o alistamento obrigatório!")
elif idade < 18:
  print("Você ainda não completou 18 anos, portanto não está hapto a se alistar")
else: 
  print(f"Você possui {idade} anos, o prazo de alistamento já passou!")
