# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
value_notaA = float(input("Digite o valor da primeira nota: "))
value_notaB = float(input("Digite o valor da segunda nota: "))

print(
    "A média aritimérica de {}! e {}! é: {}!".format(
        value_notaA, value_notaB, (value_notaA + value_notaB) / 2
    )
)
