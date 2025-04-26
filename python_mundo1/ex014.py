# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit
temp_celsius = float(input("Insira a temperatura que deseja converter: "))
temp_fahrenheit = (temp_celsius * 1.8) + 32
print(f"A temperatura {temp_celsius:.2f}C° em Fahrenheit é : {temp_fahrenheit:.2f}°F")
