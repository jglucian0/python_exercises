import def_moeda

preco = float(input("Digite o preço: "))
formatar = input("Deseja formatar os valores? [S/N] ").upper()
if formatar != 'S':
  formato = False
else:
  formato = True
print(f'A metade de {def_moeda.moeda(preco)} é {def_moeda.metade(preco, formato)}')
print(f'O dobro de {def_moeda.moeda(preco)} é {def_moeda.dobro(preco, formato)}')
print(f'O aumento de 10% é {def_moeda.aumentar(preco, 10, formato)}')
print(f'A subtração de 10% é {def_moeda.diminuir(preco, 10, formato)}')