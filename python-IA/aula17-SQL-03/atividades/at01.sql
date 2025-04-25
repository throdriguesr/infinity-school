'''
ATIVIDADE PRÁTICA 1

Suponha que você tenha uma tabela "clientes" e uma tabela "pedidos". 

Escreva uma consulta SQL que retorne o nome do cliente e o número do pedido para todos os clientes, incluindo aqueles que não fizeram nenhum pedido. 

Utilizando as mesmas tabelas de "clientes" e "pedidos", escreva uma consulta SQL que retorne o nome do cliente e o número do pedido para todos os pedidos, incluindo os pedidos que não estão associados a nenhum cliente.

'''

-- Parte 1

SELECT c.nome, p.numero_pedido
FROM clientes c
LEFT JOIN pedidos p ON c.id = p.cliente_id;

-- Parte 2

SELECT c.nome, p.numero_pedido
FROM pedidos p
LEFT JOIN clientes c ON p.cliente_id = c.id;