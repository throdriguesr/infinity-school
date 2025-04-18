'''
ATIVIDADE PRÁTICA 1

Crie um banco de dados chamado "escola" e as seguintes tabelas:

Tabela "alunos" com colunas: id_aluno, nome, idade.

Tabela "cursos" com colunas: id_curso, nome_curso, carga_horaria. 

Tabela "matriculas" com colunas: id_matricula , id_aluno id_curso, data_matricula.

'''

CREATE DATABASE escola;

USE escola;

CREATE TABLE alunos (
    id_aluno INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INT NOT NULL
);

CREATE TABLE cursos (
    id_curso INT AUTO_INCREMENT PRIMARY KEY,
    nome_curso VARCHAR(100) NOT NULL,
    carga_horaria INT NOT NULL
);

CREATE TABLE matriculas (
    id_matricula INT AUTO_INCREMENT PRIMARY KEY,
    id_aluno INT,
    id_curso INT,
    data_matricula DATE NOT NULL,
    FOREIGN KEY (id_aluno) REFERENCES alunos(id_aluno),
    FOREIGN KEY (id_curso) REFERENCES cursos(id_curso)
);