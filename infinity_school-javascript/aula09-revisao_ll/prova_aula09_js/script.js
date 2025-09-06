/*
[JSIA-A09] Crie um pequeno programa em JavaScript que simule um sistema simples de notas escolares. Seu código deve:

Declarar um objeto aluno com as seguintes propriedades:

nome (string)
idade (number)
notas (array de 3 números)


Possuir um método calcularMedia() que retorna a média das notas;

Utilizar desestruturação para acessar nome e idade;

Usar o spread operator para adicionar uma nova nota ao array original;

Criar uma função chamada verificarSituacao que:

Receba a média como parâmetro
Verifique se o aluno está aprovado (média ≥ 7) ou reprovado
Retorne uma mensagem adequada
Utilizar um loop para exibir todas as notas no console.


Exibir no console:

Nome e idade do aluno
Todas as notas
A média final
A situação (aprovado ou reprovado)
*/

// Objeto do aluno com nome, idade, notas e um jeito de calcular a média
const aluno = {
  nome: "Thiago",
  idade: 30,
  notas: [8, 6, 7],

  calcularMedia: function() {
    const soma = this.notas.reduce((acum, valor) => acum + valor, 0);
    return soma / this.notas.length;
  }
};

// Pegando nome e idade
const { nome, idade } = aluno;

// Colocando uma nova nota
aluno.notas = [...aluno.notas, 9];

// Função que diz se passou ou não
function verificarSituacao(media) {
  if (media >= 7) {
    return "Aprovado";
  } else {
    return "Reprovado";
  }
}

// Mostrando nome e idade
console.log("Nome:", nome);
console.log("Idade:", idade);

// Mostrando todas as notas
console.log("Notas do aluno:");
for (let nota of aluno.notas) {
  console.log(nota);
}

// Mostrando a média
const mediaFinal = aluno.calcularMedia();
console.log("Média final:", mediaFinal);

// Mostrando se foi aprovado ou reprovado
console.log("Situação:", verificarSituacao(mediaFinal));