# Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib
import urllib.request

try:
  site = urllib.request.urlopen('https://www.pudim.com.br')
except:
  print("ERRO! Não foi possivel acessar o site, verifique sua conexão com a internet.")
else:
  print("Tudo certo! O site esta acessivel!")
  

  