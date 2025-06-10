'''
Prova PYIA - SQL III

[PYIA-A17] Crie uma tabela chamada Estoque que contenha as seguintes colunas: 
EstoqueID, ProdutoID, FornecedorID, Quantidade e DataEntrada. 

A coluna EstoqueID deve ser um identificador único para cada registro no estoque. 

A coluna ProdutoID deve referenciar o identificador do produto correspondente na tabela de produtos, e a coluna FornecedorID deve referenciar o identificador do fornecedor na tabela de fornecedores, ambas atuando como chaves estrangeiras para estabelecer a relação com outras tabelas.

A coluna Quantidade deve indicar a quantidade de produtos recebidos, e a coluna DataEntrada deve armazenar a data em que os produtos entraram no estoque. 

Para criar esta tabela e garantir as referências corretas, é necessário definir as chaves estrangeiras para ProdutoID e FornecedorID.

Após a criação da tabela, você pode utilizar operações de banco de dados como FULL OUTER JOIN para combinar informações de diferentes tabelas, GROUP BY para agrupar dados com base em uma ou mais colunas, e ALTER TABLE para modificar a estrutura da tabela, como adicionar ou alterar colunas.

'''

CREATE TABLE Estoque (
    EstoqueID INT PRIMARY KEY, -- Identificador único para cada registro
    ProdutoID INT,             -- Identificador do produto (vem da tabela Produtos)
    FornecedorID INT,          -- Identificador do fornecedor (vem da tabela Fornecedores)
    Quantidade INT,            -- Quantidade de produtos recebidos
    DataEntrada DATE,          -- Data de entrada dos produtos no estoque
    FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID), -- Chave estrangeira para Produtos
    FOREIGN KEY (FornecedorID) REFERENCES Fornecedores(FornecedorID) -- Chave estrangeira para Fornecedores
);

-- FULL OUTER JOIN
SELECT e.EstoqueID, p.NomeProduto, f.NomeFornecedor, e.Quantidade, e.DataEntrada
FROM Estoque e
FULL OUTER JOIN Produtos p ON e.ProdutoID = p.ProdutoID
FULL OUTER JOIN Fornecedores f ON e.FornecedorID = f.FornecedorID;

-- GROUP BY
SELECT ProdutoID, SUM(Quantidade) AS Total
FROM Estoque
GROUP BY ProdutoID;

-- ALTER TABLE
ALTER TABLE Estoque
ADD COLUMN PrecoUnitario DECIMAL(10, 2);