# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma_idades = 0
nome_homem_mais_velho = ""
idade_homem_mais_velho = 0
mulheres_menos_20 = 0

for i in range(1,5):
  print(f"\nPessoa {i}:")
  nome = input("Nome: ").strip()
  idade = int(input("Idade: "))
  genero = input("Gênero (masculino/feminino): ").strip().lower()
  
  soma_idades += idade
  
  if genero == "masculino":
    if idade > idade_homem_mais_velho:
      idade_homem_mais_velho = idade
      nome_homem_mais_velho = nome
  elif genero == "feminino":
    if idade < 20:
      mulheres_menos_20 += 1

media_idades = soma_idades / 4

print("\n--- Resultado ---")
print(f"Média de idade do grupo: {media_idades:.0f} anos")
print(f"Homem mais velho: {nome_homem_mais_velho} ({idade_homem_mais_velho} anos)")
print(f"Quantidade de mulheres com menos de 20 anos: {mulheres_menos_20}")