/*
Atividade 05
Crie um array chamado numeros com os valores [1, 2, 3, 4, 5]. Usando a função
map() e uma arrow function, crie um novo array chamado dobrados que contenha
todos os números do array numeros multiplicados por 2.

Objetivo:
Praticar a criação e uso de arrow functions em operações simples.
*/

// Array de números
const numeros = [1, 2, 3, 4, 5];

// Cria um novo array com os números dobrados
const dobrados = numeros.map(num => num * 2);

// Mostra o array original
console.log("Números originais:", numeros);

// Mostra o novo array com valores dobrados
console.log("Números dobrados:", dobrados);