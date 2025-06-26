# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

# Recebe a entrada de duas notas de um aluno
primeira_nota = float(input("Insira o valor da primeira nota: "))
segunda_nota = float(input("Insira o valor da segunda nota: "))
media = (primeira_nota + segunda_nota) / 2

if (media < 5.0):
  print("Para ser aprovado você precisa de uma média acima de 5.0")
  print(f"Infelizmente você ficou com média {media:.1f} [Reprovado]")
elif (media >= 5.0 and media <= 6.9):
  print("Para ser aprovado você precisa de uma média acima de 6.9")
  print(f"Infelizmente você ficou com média {media:.1f} [Recuperação]")
else:
  print(f"Parábens! Sua média foi {media:.1f} [Aprovado]")
