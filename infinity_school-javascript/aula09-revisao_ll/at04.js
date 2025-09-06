/*
Atividade 04
Crie três arrow functions para realizar as seguintes operações
matemáticas:

soma: Recebe dois números como parâmetros e retorna a soma deles.

subtracao: Recebe dois números como parâmetros e retorna a
diferença entre eles.

multiplicacao: Recebe dois números como parâmetros e retorna o
produto deles.

Chame cada uma das funções três vezes, passando valores diferentes
como argumentos, e exiba o resultado no console.

Objetivo:
Praticar a criação e uso de arrow functions.
*/

// Arrow function que soma dois números
const soma = (a, b) => a + b;

// Arrow function que subtrai dois números
const subtracao = (a, b) => a - b;

// Arrow function que multiplica dois números
const multiplicacao = (a, b) => a * b;

// Chamadas da função soma
console.log("Soma:", soma(5, 3));
console.log("Soma:", soma(10, 7));
console.log("Soma:", soma(2, 8));

// Chamadas da função subtração
console.log("Subtração:", subtracao(9, 4));
console.log("Subtração:", subtracao(20, 5));
console.log("Subtração:", subtracao(15, 30));

// Chamadas da função multiplicação
console.log("Multiplicação:", multiplicacao(3, 4));
console.log("Multiplicação:", multiplicacao(7, 6));
console.log("Multiplicação:", multiplicacao(10, 10));