# Exercício Python 29: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

# Recebendo velocidade do veiculo
velocidade = float(input("Velocidade registrada pelo radar (Km/h): "))

# Realizando a verificação de exesso e imprimindo a resposta
if velocidade > 80:
  exesso = velocidade - 80
  multa = exesso * 7
  print("MULTADO! Você excedeu o limite de 80Km/h.")
  print(f"Valor da multa: R$ {multa:.2f}")

print("Tenha um bom dia! Dirija com segurança!")