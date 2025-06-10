'''
Imagine que você está trabalhando no desenvolvimento de um sistema de gerenciamento de vendas para uma loja. 

Você já possui algumas tabelas básicas criadas no banco de dados. 

Agora, você precisa criar consultas SQL para realizar algumas operações específicas. 

Considere as seguintes tabelas:

    Tabela "Clientes":
    Colunas: id_cliente (chave primária), nome_cliente, email_cliente.

    Tabela "Produtos":
    Colunas: id_produto (chave primária), nome_produto, preco_produto.

    Tabela "Vendas":
    Colunas: id_venda (chave primária), id_cliente (chave estrangeira referenciando a tabela "Clientes"), data_venda.

a) Crie uma consulta SQL para selecionar todos os clientes cadastrados.

b) Escreva um código SQL para inserir um novo produto chamado "Notebook" com o preço de R$ 2.500,00 na tabela "Produtos".

c) Atualize o nome do cliente com o id_cliente igual a 1 para "Maria Silva".

d) Remova todos os registros da tabela "Vendas" que ocorreram antes de 01 de janeiro de 2023.

'''

-- a) Selecionar todos os clientes cadastrados
SELECT *
FROM Clientes;

-- b) Inserir um novo produto "Notebook" com preço de R$ 2.500,00
INSERT INTO Produtos (id_produto, nome_produto, preco_produto)
VALUES (DEFAULT, 'Notebook', 2500.00);

-- c) Atualizar o nome do cliente com id_cliente = 1 para "Maria Silva"
UPDATE Clientes
SET nome_cliente = 'Maria Silva'
WHERE id_cliente = 1;

-- d) Remover todos os registros da tabela Vendas antes de 01 de janeiro de 2023
DELETE FROM Vendas
WHERE data_venda < '2023-01-01';