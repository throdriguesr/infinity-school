'''
ATIVIDADE PRÁTICA 3

Suponha que você tenha tabelas "Pessoas" e "Documentos de Identidade" com um relacionamento um-para-um. 

Escreva uma consulta para recuperar o nome de cada pessoa e o número do documento de identidade, se estiverem disponíveis.

'''

SELECT p.nome, d.numero_documento
FROM Pessoas p
LEFT JOIN Documentos d ON p.id = d.pessoa_id;