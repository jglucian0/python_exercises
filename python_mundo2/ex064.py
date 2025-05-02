# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).


soma = 0
count = 0
escolha_parar = False

print("\nPara encerrar digite [999]")
while escolha_parar == False:
  numero_escolhido = int(input("Insira um número qualquer: "))
  
  if numero_escolhido == 999:
    escolha_parar = True
  else:
    numero = numero_escolhido
    soma += numero
    count += 1
  
print(f"A soma dos {count} números digitados foi {soma}")