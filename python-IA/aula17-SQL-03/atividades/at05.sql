'''
ATIVIDADE PRÁTICA 5

Dado um cenário com tabelas "Músicos" e "Bandas" com um relacionamento muitos-para-muitos.

Escreva uma consulta que liste o nome de cada músico e as bandas em que eles tocam.

'''

SELECT m.nome AS nome_musico, b.nome AS nome_banda
FROM Musicos m
JOIN Musico_Banda mb ON m.id = mb.musico_id
JOIN Bandas b ON mb.banda_id = b.id;