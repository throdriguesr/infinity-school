'''
[PYIA-A15] Crie uma tabela chamada Clientes com as colunas ID, Nome, Idade e Cidade. 

Defina a coluna ID como a chave primária e autoincrementável.

'''

CREATE TABLE Clientes (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100),
    Idade INT,
    Cidade VARCHAR(100)
);