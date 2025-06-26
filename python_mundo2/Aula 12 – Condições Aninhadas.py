# Nessa aula, vamos aprender como criar estruturas condicionais aninhadas, usando os comandos if.. elif.. else em programas Python.

# Condições aninhadas são basicamente "if dentro de if" — ou seja, quando uma verificação só acontece se outra já tiver sido verdadeira antes.
# Exemplo 1
tem_ingresso = True
idade = 20

if tem_ingresso: # Primeiro o Python verifica: tem_ingresso == True
    if idade >= 18: # segundo if (aninhado) Aí sim ele checa se a idade é maior ou igual a 18.
        print("Pode entrar no cinema.")
    else:
        print("Você precisa ter 18 anos ou mais.")
else:
    print("Você precisa de um ingresso.")

