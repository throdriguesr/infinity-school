// Atividade 05:
// Crie três funções anônimas e atribua-as a variáveis para realizar as seguintes operações matemáticas:
//
// Soma: A função deve receber dois números e retornar a soma deles.
// Subtração: A função deve receber dois números e retornar a subtração do primeiro pelo segundo.
// Multiplicação: A função deve receber dois números e retornar o produto deles.
//
// Em seguida:
// Chame cada função anônima passando diferentes valores e exiba o resultado no console.
//
// Objetivo:
// Praticar o uso de funções anônimas, atribuindo-as a variáveis para realizar diferentes operações matemáticas.

// Função anônima para soma
const soma = function(a, b) {
  return a + b;
};

// Função anônima para subtração
const subtracao = function(a, b) {
  return a - b;
};

// Função anônima para multiplicação
const multiplicacao = function(a, b) {
  return a * b;
};

// Chamando as funções com diferentes valores
console.log("Soma: ", soma(10, 5));
console.log("Subtração: ", subtracao(20, 7));
console.log("Multiplicação: ", multiplicacao(4, 3));

// Chamadas extras
console.log("Soma: ", soma(2, 9));
console.log("Subtração: ", subtracao(15, 15));
console.log("Multiplicação: ", multiplicacao(5, 0));