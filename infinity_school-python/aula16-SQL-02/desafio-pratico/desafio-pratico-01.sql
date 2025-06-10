'''
DESAFIO PRÁTICO

Sistema de gerenciamento de vendas

Você está criando um banco de dados para gerenciar vendas de produtos em uma loja online.

Você precisa projetar o esquema do banco de dados e escrever consultas SQL para atender a várias necessidades da loja. 

Aqui estão os requisitos:

Crie um banco de dados chamado "loja_online" e as seguintes tabelas:

    Produtos: Armazena informações sobre produtos, incluindo um ID, nome, preço e quantidade em estoque.

    Clientes: Armazena informações sobre os clientes, incluindo um ID, nome, endereço de e-mail e histórico de compras.

    Pedidos: Registra informações sobre os pedidos feitos pelos clientes, incluindo um ID, data do pedido, ID do cliente e status do pedido.

    itens_Pedido: Registra os produtos incluídos em cada pedido, incluindo um ID, ID do pedido, ID do produto e quantidade.

'''

CREATE DATABASE loja_online;

USE loja_online;

CREATE TABLE Produtos (
  id_produto INT AUTO_INCREMENT PRIMARY KEY,
  nome_produto VARCHAR(255),
  preco_produto DECIMAL(10,2),
  quantidade_estoque INT
);

CREATE TABLE Clientes (
  id_cliente INT AUTO_INCREMENT PRIMARY KEY,
  nome_cliente VARCHAR(255),
  email_cliente VARCHAR(255),
  historico_compras TEXT
);

CREATE TABLE Pedidos (
  id_pedido INT AUTO_INCREMENT PRIMARY KEY,
  data_pedido DATE,
  id_cliente INT,
  status_pedido VARCHAR(50),
  CONSTRAINT fk_pedidos_cliente
    FOREIGN KEY (id_cliente)
    REFERENCES Clientes(id_cliente)
);

CREATE TABLE itens_Pedido (
  id_item INT AUTO_INCREMENT PRIMARY KEY,
  id_pedido INT,
  id_produto INT,
  quantidade INT,
  CONSTRAINT fk_item_pedido_pedido
    FOREIGN KEY (id_pedido)
    REFERENCES Pedidos(id_pedido),
  CONSTRAINT fk_item_pedido_produto
    FOREIGN KEY (id_produto)
    REFERENCES Produtos(id_produto)
);