# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times_brasileirao = (
    'Palmeiras', 'Flamengo', 'Atlético-MG', 'Grêmio', 'Botafogo',
    'Bragantino', 'Athletico-PR', 'Internacional', 'Fortaleza', 'São Paulo',
    'Cuiabá', 'Corinthians', 'Bahia', 'Cruzeiro', 'Santos',
    'Vasco', 'Goiás', 'Coritiba', 'América-MG', 'Chapecoense'
)

top_five = times_brasileirao[0:5]
bottom_four = times_brasileirao[-4:]
teams_alphabetical = sorted(times_brasileirao)
chapecoense_position = times_brasileirao.index("Chapecoense") + 1

print(top_five)
print(bottom_four)
print(teams_alphabetical)
print(chapecoense_position)
