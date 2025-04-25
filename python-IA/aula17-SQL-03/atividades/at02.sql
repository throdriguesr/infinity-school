'''
ATIVIDADE PRÁTICA 2

Suponha que você tenha uma tabela "vendedores" e uma tabela "vendas". 

Escreva uma consulta SQL que retorne o nome do vendedor e o valor da venda para todas as vendas e todos os vendedores, incluindo os vendedores que não fizeram nenhuma venda e as vendas não associadas a nenhum vendedor.

'''

SELECT vendedores.nome, vendas.valor
FROM vendedores
FULL OUTER JOIN vendas ON vendedores.id = vendas.vendedor_id;