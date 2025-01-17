# Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

# Coletando a entradam da frase
frase = str(input("Digita uma frase qualquer: ")).upper().strip()

# Realizando a filtragens da letra "A",aplicando formatação e imprimindo os resultados
print("A letra 'A' aparece {} vezes na frase".format(frase.count("A")))
print("A primeira letra 'A' apareceu na posição {}".format(frase.find("A") + 1))
print("A última letra 'A' apareceu na posição {}".format(frase.rfind("A") + 1))
