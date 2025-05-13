# Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python.
# As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

dados = list()
pessoas = list()
dados.append('Pedro')
dados.append(25)

pessoas.append(dados[:]) # Fatiamento/Cópia completa da estrutura

# Listas compostas
pessoas_list = [['Pedro', 25],['Maria',18]]
print(pessoas_list[1][0])