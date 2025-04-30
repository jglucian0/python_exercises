# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro_termo = int(input("Insira o primeiro termo: "))
razao = int(input("Insira a razão: "))
termo = primeiro_termo
count = 1

while count <= 10:
  termo += razao
  if count == 10:
    print(termo, end= '. Acabou!')
  else:
    print(termo, end= ', ')
  count += 1