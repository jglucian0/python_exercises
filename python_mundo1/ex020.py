# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
# Importando a biblioteca ramdom
import random

# Coletando a entrada do nomes dos alunos
primeiro_aluno = str(input("Insira o nome do primeiro aluno: "))
segundo_aluno = str(input("Insira o nome do segundo aluno: "))
terceiro_aluno = str(input("Insira o nome do terceiro aluno: "))
quarto_aluno = str(input("Insira o nome do quarto aluno: "))

# Armazenando os nomes em uma lista [] e realizando o sorteiro com shuffle
lista_alunos = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]
random.shuffle(lista_alunos)

# Imprimindo a sequência sorteada
print(f"A sequência sorteada foi: {lista_alunos}")
