/*
Atividade 04
Crie um array chamado livros, onde cada elemento do array é um
objeto representando um livro, com as seguintes propriedades:

titulo: string com o título do livro.
autor: string com o nome do autor.

Após criar o array:
- Exiba no console todos os títulos dos livros.
- Adicione um novo objeto representando outro livro ao array.
- Exiba no console a lista completa de livros após a adição.

Objetivo:
Praticar a criação, manipulação e iteração de um array de objetos
*/

let livros = [
  { titulo: "Dom Casmurro", autor: "Machado de Assis" },
  { titulo: "O Hobbit", autor: "J.R.R. Tolkien" },
  { titulo: "1984", autor: "George Orwell" }
];

for (let i = 0; i < livros.length; i++) {
  console.log(livros[i].titulo);
}

livros.push({ titulo: "Harry Potter", autor: "J.K. Rowling" });

console.log(livros);