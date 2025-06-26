# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

lista = tuple(int(input("Insira um valor qualquer: ")) for _ in range(4))
count_9 = lista.count(9)

print(f"A lista formada foi {lista}") 
print(f"Existem {count_9} números 9")
if 3 in lista:
  pos_3 = lista.index(3) + 1
  print(f"O número 3 apareceu na {pos_3}° posição")
else:
  print("O número 3 não foi digitado")
  
print(f"Os números pares foram ", end ="")
for n in lista:
  if n % 2 == 0:
    print(n, end=" ")
    
