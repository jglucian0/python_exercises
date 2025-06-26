# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

lista_alunos = {}
lista_alunos['nome'] = str(input("Insira o nome do aluno: ")).strip().capitalize()
lista_alunos['media'] = float(input("Insira a média do aluno: "))

if lista_alunos['media'] < 5.0:
  lista_alunos['situacao'] = 'Reprovado'
elif lista_alunos['media'] <= 5.0 or lista_alunos['media'] <= 6.9:
  lista_alunos['situacao'] = 'Recuperação'
else:
  lista_alunos['situacao'] = 'Aprovado'
  
print(f"\nNome do aluno > {lista_alunos['nome']}")
print(f"Média do aluno > {lista_alunos['media']}")
print(f"Status do aluno > {lista_alunos['situacao']}")
