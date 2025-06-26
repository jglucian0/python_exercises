# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

lista_alunos = []

while True:
  nome_aluno = str(input("Insira o nome do aluno: ")).strip()
  nota_A = float(input("Insira a primeira nota: "))
  nota_B = float(input("Insira a segunda nota: "))
  media = (nota_A + nota_B) / 2
  lista_alunos.append([nome_aluno, nota_A, nota_B, media])
  
  if str(input("Deseja inserir outro aluno? [S/N] ")).strip().upper() != 'S':
    break

print("\nBOLETIM:")
print(f"{'Nº':<4}{'Nome':<10}{'Média':>6}")
print("-" * 22)
for i, aluno in enumerate(lista_alunos):
  print(f"{i:<4}{aluno[0]:<10}{aluno[3]:>4.1f}")
  
while True:
  opcao = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
  
  if opcao == 999:
        print("Finalizando...")
        break
  if 0 <= opcao < len(lista_alunos):
    print(f"As notas de {lista_alunos[opcao][0]} são: {lista_alunos[opcao][1:3]}")
  else:
    print("Aluno não encontrado. Tente novamente.")
  