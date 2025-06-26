# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
# Importando a biblioteca Math
from math import radians, sin, cos, tan

# Colentando o valor do ângulo escolhido pelo usuario
angulo_graus = int(input("Insira o valor do ângulo: "))

# Convertendo para radianos (necessário, pois math usa radianos)
angulo_radianos = radians(angulo_graus)

# Calculando seno, cosseno e tangente
seno = sin(angulo_radianos)
cosseno = cos(angulo_radianos)
tangente = tan(angulo_radianos)

# Imprimindo os resultados
print(
    f"O resultados para {angulo_graus}° são: \nSeno {seno:.2f} \nCosseno {cosseno:.2f} \nTangente {tangente:.2f}"
)
