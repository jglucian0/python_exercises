# Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em Python.
# Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves literais.

# Lista com indices numéricos
dadosl = list()
dadosl.append('Pedro')
dadosl.append(25)
print(dadosl[0]) # Pedro
print(dadosl[1]) # 25

# Dicionaios com indices literais
dados = dict()
dados = {'nome':'Pedro', 'idade':25}
print(dados['nome']) # Pedro
print(dados['idade']) # 25

dados['genero'] = 'M'
del dados['idade']

filme = {'titulo':'Star Wars',
         'ano': 1977,
         'diretor':'George Lucas'
        }

print(filme.values()) # Retorna todos os valores do dicionário ex: StarWars, 1977, George Lucas
print(filme.keys()) # Retorna todas as chaves do dicionário ex: titulo, ano, diretor
print(filme.item()) # Retorna o dicionário inteiro
filme.copy() # Copia elementos, similar ao fatiamento de lista [:]


for key, value in filme.items():
  print(f'O {key} é {value}')
  
pessoas = {'nome': 'Gustavo', 'genero': 'M', 'idade': 25}
print(pessoas['nome'])
print(f"O {pessoas['nome']} tem {pessoas['idade']}")
print(pessoas.keys()) # nome, sexo, idade
print(pessoas.values()) # Gustavo, 'M', 'idade'
  
