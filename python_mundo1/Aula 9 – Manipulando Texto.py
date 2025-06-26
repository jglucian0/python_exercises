# Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o Fatiamento de String,
# Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().#

frase = "Curso em Video Python"

# Técnica de Fatiamento
# A seleção de fatiamento inicia no dígito [9] porém é preciso usar uma casa a mais, pois o ultimo dígito [14] será anulado
frase[9:14]
# Quanto adiciono um terceiro dígito ao fatiamento o python considera o dígito [2] como uma cadência para ignorar "ex: V d o P t o"
frase[9:14:2]
# Quando o dígito de inicio é omitido ele considera como 0
frase[:20]
# Quando o dígito final é omitido ele considera até o ultimo dígito existente
frase[0:]


# Técnica de Análise
# Para strings, len retorna o número de caracteres (incluindo espaços e símbolos).
len(frase)
# Conta quantas vezes um determinado caractere ou substring aparece na string.
frase.count("o")
# usada para localizar a posição de uma substring dentro de uma string. (-1 = inexistente)
"Cruso" in frase  # True ou Falso
frase.find("Video")

# Técnica de Transformação
# Replace é usada para substituir partes de uma string por outra.
frase.replace("Python", "Android")
# Usada para converter todos os caracteres de uma string em letras maiúsculas.
frase.upper()
# Usado para converter todos os caracteres de uma string para letras minúsculas.
frase.lower()
# Usado para transformar apenas o primeiro caractere de uma string em maiúscula.
frase.capitalize()
# Usado para capitalizar a primeira letra de cada palavra em uma string.
frase.title()
# Usado para remover espaços em branco do início e do final de uma string.
frase.strip()
frase.rstrip()  # Remove apenas espaços da direita
frase.lstrip()  # Remove apenas espaços da esquerda

# Técnica de Divisão
# Usado para dividir uma string em uma lista de substrings, com base em um delimitador especificado (por padrão, um espaço em branco).
frase.split()

# Técnica de Junção
# Usado para concatenar uma sequência de strings, colocando um separador entre elas.
"-".join(frase)
