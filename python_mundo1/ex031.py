# Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

# Coletando a entrada da distância em km
distancia = float(input("Qual a distância da viagem (Km)? "))

# Verificando se a distancia excede 200km e imprimindo com valor promocional ou não
if distancia > 200:
  valor_passagem = 0.45 * distancia
else:
  valor_passagem = 0.50 * distancia

print(f"Você está prestes a iniciar uma viagem de {distancia:.2f}Km")
print(f"O valor da passagem custará R${valor_passagem:.2f}")