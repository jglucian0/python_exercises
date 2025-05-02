# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média
# entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

exit_action  = False
max_number = min_number = None
calc_total = calc_media = count_numbers = 0

while exit_action == False:
  user_number  = int(input("Insira um número qualquer: "))
  count_numbers += 1
  
  if max_number is None or user_number > max_number:
    max_number = user_number
  elif min_number is None or user_number < min_number:
    min_number = user_number
    
  calc_total += user_number
  calc_media = calc_total / count_numbers
  
  exit_option = str(input("Deseja continuar? [S/N] ")).upper()
  if exit_option == "N":
    exit_action = True
  elif exit_option != "S":
    print("Opção inválida... Digite apenas [S/N] ")
    exit_option = str(input("Deseja continuar? [S/N] ")).upper()
    if exit_option != "S" or exit_option == "N":
      print("Programa encerrado... Digito inválido.")
      exit_action = True

print(f"Você digitou {count_numbers} números e a média foi {calc_media:.2f}")
print(f"O MAIOR numero registrado é {max_number} e o MENOR {min_number}")
    
