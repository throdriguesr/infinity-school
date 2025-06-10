'''
DESAFIO PRÁTICO

Sistema de uma escola 

Crie um banco de dados para um sistema de uma escola, esse banco de dados ficará responsável por persistir os dados sobre alunos, professores, turmas e disciplinas.

Para os alunos é importante que contenha um número de matrícula, o nome, a idade, e o endereço.

Para os professores, deverá conter um número de matrícula, nome, especialidade e endereço. 

Para a turma deverá conter um identificador, horário de início e dia de semana.

Para disciplina é importante que contenha um identificador, nome e quantidade de aulas.

'''

CREATE DATABASE escola;

USE escola;

CREATE TABLE alunos (
    matricula INT PRIMARY KEY,
    nome VARCHAR(100),
    idade INT,
    endereco VARCHAR(200)
);

CREATE TABLE professores (
    matricula INT PRIMARY KEY,
    nome VARCHAR(100),
    especialidade VARCHAR(100),
    endereco VARCHAR(200)
);

CREATE TABLE turmas (
    id INT PRIMARY KEY,
    horario_inicio TIME,
    dia_semana VARCHAR(20)
);

CREATE TABLE disciplinas (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    quantidade_aulas INT
);