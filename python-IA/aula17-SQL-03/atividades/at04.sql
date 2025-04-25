'''
ATIVIDADE PRÁTICA 4

Suponha que você tenha tabelas "Autores" e "Livros" com um relacionamento um-para-muitos. 

Escreva uma consulta que retorne o nome de cada autor e os títulos dos livros que eles escreveram.

'''

SELECT a.nome, l.titulo
FROM Autores a
JOIN Livros l ON a.id = l.autor_id;