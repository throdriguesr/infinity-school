/*
Atividade 03
Crie um objeto chamado livro que contenha as seguintes propriedades:

titulo: uma string representando o título do livro.
autor: uma string com o nome do autor.
ano: um número representando o ano de publicação.
editora: uma string com o nome da editora.

Utilize a desestruturação para extrair as propriedades titulo e autor do objeto livro.
Em seguida, exiba essas propriedades no console.

Objetivo:
Praticar a desestruturação de objetos em JavaScript, extraindo propriedades e definindo valores padrão.
*/

let livro = {
    titulo: "O Senhor dos Anéis",
    autor: "J.R.R. Tolkien",
    ano: 1954,
    editora: "Allen & Unwin"
};

let { titulo, autor } = livro;

console.log("Título:", titulo);
console.log("Autor:", autor);