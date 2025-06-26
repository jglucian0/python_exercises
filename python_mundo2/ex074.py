# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

# num_random = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
num_random = tuple(randint(1, 10) for _ in range(5))

print(f"A seguência gerada foi {num_random}")
print(f"O maior número foi {max(num_random)}")
print(f"O menor número foi {min(num_random)}")