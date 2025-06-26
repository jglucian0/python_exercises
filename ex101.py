# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor
# literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

from datetime import date

def voto(idade):
  if idade < 16:
    return "NEGADO"
  elif idade >= 18 and idade <= 70:
    return "OBRIGATÓRIO"
  elif idade >= 16 or idade == 17 or idade < 70:
    return "OPCIONAL"
 
idade = (date.today().year) - (int(input("Insira o ano de nascimento: ")))
print(f'Sua idade é {idade} e seu status para votação nas eleições é: [{voto(idade)}]')
