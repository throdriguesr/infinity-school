'''
DESAFIO PRÁTICO

Banco de dados de uma biblioteca

Suponha que você esteja gerenciando um banco de dados para uma biblioteca. 

O banco de dados contém as seguintes tabelas:

Tabela "Livros" com as seguintes colunas:

- livro_id (Chave Primária)
- título
- autor_id (Chave Estrangeira relacionando-se à tabela "Autores")
- ano_publicação
- gênero

Tabela "Autores" com as seguintes colunas:

- autor_id (Chave Primária)
- nome_autor

Tabela "Empréstimos" com as seguintes colunas:

- emprestimo_id (Chave Primária)
- livro_id (Chave Estrangeira relacionando-se à tabela "Livros")
- data_emprestimo
- data_devolução

Seu desafio é escrever uma consulta SQL que retorna o nome de cada autor, o título do livro emprestado e a data de empréstimo. 

No entanto, você precisa considerar apenas os autores cujos livros foram emprestados. 

Além disso, a consulta deve listar os autores em ordem alfabética e os livros em ordem de data de empréstimo crescente.

'''

SELECT a.nome_autor, l.titulo, e.data_emprestimo
FROM Autores a
JOIN Livros l ON a.autor_id = l.autor_id
JOIN Emprestimos e ON l.livro_id = e.livro_id
ORDER BY a.nome_autor ASC, e.data_emprestimo ASC;