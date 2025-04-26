# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
# Importando biblioteca Math
import random

# Coletando o nome dos quatro alunos
primeiro_alunos = str(input("Digite o nome do 1° aluno: "))
segundo_aluno = str(input("Digite o nome do 2° aluno: "))
terceiro_alunos = str(input("Digite o nome do 3° aluno: "))
quarto_alunos = str(input("Digite o nome do 4° aluno: "))

# Armazenando os nomes coletados em uma lista
lista_alunos = [primeiro_alunos, segundo_aluno, terceiro_alunos, quarto_alunos]

# Utilzia o ramdom choice para sortear um nome dentro de uma lista
resultado_sorteio = random.choice(lista_alunos)

# Imprime o resultado
print(f"O aluno sorteado para apagar o quadro foi: {resultado_sorteio}!")
