'''
ATIVIDADE PRÁTICA 1

Crie uma tabela "pedidos" com as colunas "id_pedido", "id_cliente" e "data_pedido". 

Adicione uma constraint de chave estrangeira na coluna "id_cliente" para garantir que um pedido só possa ser feito por um cliente existente na tabela "clientes".

'''

CREATE TABLE pedidos (
  id_pedido INT PRIMARY KEY,
  id_cliente INT,
  data_pedido DATE,
  CONSTRAINT fk_cliente
    FOREIGN KEY (id_cliente)
    REFERENCES clientes(id_cliente)
);