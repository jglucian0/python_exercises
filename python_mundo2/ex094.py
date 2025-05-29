# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

lista_pessoas = []
soma_idades = 0

while True:
  pessoa = {}
  
  pessoa['nome'] = str(input("Nome: ")).capitalize().strip()
  while True:
    pessoa['sexo'] = str(input("Sexo [M/F]: ")).upper()[0]
    if pessoa['sexo'] in "MF":
      break
    print("ERRO! Digite apenas M ou F")
  pessoa['idade'] = int(input("Idade: "))
  soma_idades += pessoa['idade']
  
  lista_pessoas.append(pessoa.copy())
  
  opcao_sair = str(input("Deseja inserir outra pessoa? [S/N]")).upper().strip()
  if opcao_sair != 'S':
    break
  
media_idade = soma_idades / len(lista_pessoas)
print(f"Foram cadastradas {len(lista_pessoas)} pessoas")
print(f"A média das idades foi {media_idade:5.2f} anos")
print(f"As mulheres cadastradas foram: ", end="")

for p in lista_pessoas:
  if p['sexo'] in "F":
     print(f"{p['nome']}", end=', ')
print()

print(f"As pessoas que estão com idade acima da média são(é): ", end="")

for p in lista_pessoas:
  if p['idade'] >= media_idade:
    print(f"{pessoa['nome']}", end=' ')
print()