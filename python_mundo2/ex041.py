# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from datetime import datetime
ano_atual = datetime.now().year

# Recebe o ano de nascimento de um atle
ano_nascimento = int(input("Insira seu ano de nascimento: "))
idade = ano_atual - ano_nascimento

# Realiza a verificação baseado na idade do atleta e informa sua categoria
if idade <=9:
  print(f"Sua idade é {idade} anos sua categoria é Mirin")
elif idade <= 14:
  print(f"Sua idade é {idade} anos sua categoria é Infantil")
elif idade <= 19:
  print(f"Sua idade é {idade} anos sua categoria é Júnior")
elif idade <= 25:
  print(f"Sua idade é {idade} anos sua categoria é Sênior")
elif idade > 25:
  print(f"Sua idade é {idade} anos sua categoria é Master")