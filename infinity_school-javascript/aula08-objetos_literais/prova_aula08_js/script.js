/*
[JSIA-A08]  Explique o que são objetos literais em JavaScript e mostre um exemplo prático de um objeto chamado aluno, que contenha as seguintes propriedades e métodos:

- nome (string)
- notas (array de números)
- calcularMedia() (método que retorna a média das notas)

Além disso, utilize a desestruturação para acessar o nome do aluno, e o spread operator para adicionar uma nova nota ao array original.
*/

/*
Resposta: 

O que são objetos literais?

Em JavaScript, objetos literais são criados de forma direta, usando {} para definir propriedades e métodos.
Eles permitem organizar dados (como nome, idade, notas) e funções relacionadas em uma única estrutura.
*/

// Criando um objeto literal
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
  }
};

// --- Usando desestruturação para acessar o nome ---
let { nome } = aluno;
console.log("Nome do aluno:", nome);

// --- Usando spread operator para adicionar uma nova nota ---
let novasNotas = [...aluno.notas, 10];
console.log("Notas originais:", aluno.notas);
console.log("Notas atualizadas:", novasNotas);

// --- Calculando a média das notas originais ---
console.log("Média das notas:", aluno.calcularMedia());