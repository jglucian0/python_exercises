# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

count_olderage = count_man = count_homan_20 = count_people = 0

while True:
  count_people += 1
  user_idade = int(input(f"\nIdade da {count_people}° pessoa: "))
  user_genero = str(input(f"Gênero da {count_people}° pessoa [M/F]: "))
  
  if user_idade >= 18:
    count_olderage += 1

  if user_genero == "M":
    count_man += 1
  elif user_genero == "F" and user_idade < 20:
    count_homan_20 += 1
  
  option_add = str(input("\nDeseja adicionar mais uma pessoa? [S/N] ")).upper()
  
  if option_add != "S":
    print(f"\nVocê inseriu {count_people} pessoas, sendo {count_olderage} maiores de 18 anos")
    print(f"Foram contabilizados {count_man} Homens e {count_homan_20} Mulheres abaixo de 20 anos")
    break