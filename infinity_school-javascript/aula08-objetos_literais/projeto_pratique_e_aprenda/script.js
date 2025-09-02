/*
PRATIQUE E APRENDA

Crie um objeto chamado aluno que deve conter as seguintes propriedades:
- nome: uma string com o nome do aluno.
- notas: um array com as notas do aluno.

Além das propriedades, adicione os seguintes métodos ao objeto aluno:

- calcularMedia(): Este método deve calcular e retornar a média das notas armazenadas no array notas.
- adicionarNota(nota): Este método deve permitir adicionar novas notas ao array de notas do aluno.

Após criar o objeto:
- Calcule a média das notas usando o método calcularMedia() e exiba o resultado no console.
*/

// Criando o objeto aluno
let aluno = {
  nome: "Thiago",
  notas: [8, 7, 9],

  // Método para calcular a média
  calcularMedia: function () {
    let soma = 0;
    for (let i = 0; i < this.notas.length; i++) {
      soma += this.notas[i];
    }
    return soma / this.notas.length;
  },

  // Método para adicionar uma nova nota
  adicionarNota: function (nota) {
    this.notas.push(nota);
  }
};

// Usando o método para adicionar uma nota nova
aluno.adicionarNota(10);

// Calculando a média
let media = aluno.calcularMedia();
console.log("Média do aluno:", media);