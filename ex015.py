# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

# Pergunta ao usuário a quantidade de km percorridos e os dias utilizados
km_percorridos = int(input("Insira quantos km foram percorridos com o veículo: "))
dias_utilizados = int(
    input("Insira a quantidade de dias que o veículo foi utilizado: ")
)

# Calcula os custos
custo_km = 0.15 * km_percorridos
custo_dias = 60 * dias_utilizados
valor_total = custo_km + custo_dias

# Exibe o valor total
print(f"O valor total a ser pago pelo aluguel é: R$ {valor_total:.2f}")
