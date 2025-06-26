# Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo mais sobre Interactive Help em Python,
# o uso de docstrings para documentar nossas funções, argumentos opcionais para dar mais dinamismo em funções Python, escopo de variáveis e retorno de resultados.

# Interactive help
help(str)
print(input.__doc__)


# Docstrings
def contador(i, f, p):
  """
  -> Faz uma contagem e mostra na tela.
  :param i: inicio da contagem
  :param f: fim da contagem
  :param p: passo da contagem
  :return: sem retorno
  """
  c = i
  while c <= f:
    print(f'{c} ', end='')
    c += p
  print('FIM!')

contador(2, 10, 2)
help(contador)


# Parâmetros opcionais
def somar(a,b,c=0):
  s = a + b + c
  print(f'A soma vale {s}')

somar(3,2,5)
somar(3,2) # Programa quebra sem o parâmetro opcional c=0


# Escopo de variáveis
def teste(b):
  global a # define A como global para utilizar a variavel fora do escopo
  a = 8
  b += 4
  c = 2
  print(f'A dentro vale {a}')
  print(f'B dentro vale {b}')
  print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A dentro vale {a}')


# Retornando valores "return"
def somar(a=0,b=0,c=0):
  s = a + b + c
  return s

r1 = somar(3,2,5)
r2 = somar(6,4,5)
print(f'Meus cálculos foram {r1} e {r2}')