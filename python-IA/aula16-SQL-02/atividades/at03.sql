'''
ATIVIDADE PRÁTICA 3

Adicione uma constraint de restrição única na coluna "email" da tabela "clientes" para garantir que nenhum cliente possa ter o mesmo endereço de e-mail.

'''

ALTER TABLE clientes
ADD CONSTRAINT uq_email
  UNIQUE (email);