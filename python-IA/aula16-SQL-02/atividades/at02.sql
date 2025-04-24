'''
ATIVIDADE PRÁTICA 2

Crie uma tabela "produtos" com as colunas "id_produto", "nome_produto" e "preco". 

Adicione uma constraint de verificação para garantir que o preço do produto seja maior que zero.

'''

CREATE TABLE produtos (
  id_produto INT PRIMARY KEY,
  nome_produto VARCHAR(255),
  preco DECIMAL(10,2),
  CONSTRAINT chk_preco_positivo
    CHECK (preco > 0)
);