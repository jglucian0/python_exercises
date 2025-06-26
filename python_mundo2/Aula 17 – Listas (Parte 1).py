# Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python.
# As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

# Variáveis Compostas (Listas)
lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
lanche.append('lasanha')
lanche.insert(2, 'cachorro-quente')
print(lanche)

if 'suco' in lanche:
  # del lanche[3]
  # lanche.pop() # Remove o último elemento
  lanche.remove('suco')
print(lanche)

valores = list(range(1, 11)) # Define uma lista com range
valores.sort(reverse=True) # Ordena os valores da lista de forma inversa
print(valores)
