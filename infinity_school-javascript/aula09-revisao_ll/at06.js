/*
Atividade 06
Crie um array chamado numeros com os valores [1, 2, 3, 4, 5].

Usando o método reduce(), calcule a soma de todos os números do array e
armazene o resultado em uma variável chamada somaTotal.

Usando o método reduce() novamente, calcule o produto de todos os números
do array (multiplicação) e armazene o resultado em uma variável chamada
produtoTotal.

Exiba ambos os resultados no console.

Objetivo:
Praticar o uso do método reduce().
*/

// Array de números
const numeros = [1, 2, 3, 4, 5];

// Soma de todos os números
const somaTotal = numeros.reduce((acumulador, valor) => acumulador + valor, 0);

// Produto de todos os números
const produtoTotal = numeros.reduce((acumulador, valor) => acumulador * valor, 1);

// Exibe a soma
console.log("Soma total:", somaTotal);

// Exibe o produto
console.log("Produto total:", produtoTotal);