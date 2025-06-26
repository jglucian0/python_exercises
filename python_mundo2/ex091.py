# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

import random
import time
from operator import itemgetter

number_dict = {'jogador 1': random.randint(1, 6),
                'jogador 2': random.randint(1, 6),
                'jogador 3': random.randint(1, 6),
                'jogador 4': random.randint(1, 6),}
ranking = list()

print("Jogando...")
time.sleep(0.5)

for k, i in number_dict.items():
  print(f"O jogador {k} tirou {i}")
  time.sleep(0.7)
ranking = sorted(number_dict.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
  print(f"Ranking {i+1}° Lugar: {v[0]} com {v[1]}")
  
  


  
