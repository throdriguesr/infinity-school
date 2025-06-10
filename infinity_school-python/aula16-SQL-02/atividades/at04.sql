'''
ATIVIDADE PRÁTICA 4

Escreva uma consulta que recupere o nome de todos os alunos que tenham mais de 20 anos e que estejam matriculados em cursos de "Matemática". 

Use uma subconsulta para realizar essa tarefa.

'''

SELECT nome
FROM alunos
WHERE idade > 20
  AND curso_id = (
    SELECT id_curso
    FROM cursos
    WHERE nome = 'Matemática'
  );