# Nessa aula, vamos aprender como utilizar a instrução break e os loopings infinitos a favor das nossas estratégias de código.
# É muito importante saber usar o break no Python, já que em alguns casos precisamos interromper um laço no meio do caminho.
# Além disso, vamos aprender como trabalhar com as novas fstrings do Python.

count = 0

while True:  # loop infinito
    print(f"Contador: {count}")
    count += 1

    if count == 5:
        print("Condição de parada atingida. Encerrando o loop.")
        break  # sai do loop quando contador chega a 5