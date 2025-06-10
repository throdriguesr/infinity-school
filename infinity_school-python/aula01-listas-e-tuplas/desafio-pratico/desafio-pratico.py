'''
Suponha que você está gerenciando uma competição esportiva e tem
uma lista de tuplas representando os resultados das equipes em
diferentes modalidades. Cada tupla contém o nome da equipe, seguido
por uma lista de pontuações obtidas em cada rodada da competição.

1.Calcule a média das pontuações de cada equipe e armazene esses
valores em uma nova lista chamada medias.
2.Ordene a lista medias em ordem decrescente.
3.Crie uma nova lista chamada classificacao que contém tuplas, onde
cada tupla contém o nome da equipe e sua média de pontuações.
4.Exiba na tela a classificação final das equipes, mostrando o nome da
equipe e sua média, da equipe com a pontuação mais alta para a
mais baixa.

'''

equipes = [
    ('Equipe A', [8, 9, 7, 10]),
    ('Equipe B', [7, 6, 8, 9]),
    ('Equipe C', [9, 10, 9, 10]),
    ('Equipe D', [6, 5, 7, 8])
]

medias = []

for equipe in equipes:
    nome = equipe[0]
    pontuacoes = equipe[1]
    media = sum(pontuacoes) / len(pontuacoes)
    medias.append(media)

medias.sort(reverse=True)

classificacao = []

for media in medias:
    for equipe in equipes:
        nome = equipe[0]
        pontuacoes = equipe[1]
        media_equipe = sum(pontuacoes) / len(pontuacoes)
        if media == media_equipe:
            classificacao.append((nome, media))
            equipes.remove(equipe)

print("Classificação Final:")
for equipe, media in classificacao:
    print(f"{equipe}: {media:.2f}")