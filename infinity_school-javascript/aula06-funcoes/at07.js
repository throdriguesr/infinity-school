// Atividade 07:
// Crie uma função arrow chamada filtrarPares que receba um array de números
// como parâmetro e retorne um novo array contendo apenas os números pares.
//
// Em seguida, crie outra função arrow chamada calcularMedia que receba um
// array de números e retorne a média desses números.
//
// Faça o seguinte:
// 1. Chame a função filtrarPares passando um array de números.
// 2. Use o resultado de filtrarPares como argumento para a função calcularMedia.
// 3. Exiba no console o array filtrado e a média dos números pares.
//
// Objetivo:
// Praticar o uso de arrow functions com lógica condicional e manipulação de arrays.

// Arrow function para filtrar números pares
const filtrarPares = (numeros) => {
  return numeros.filter((num) => num % 2 === 0);
};

// Arrow function para calcular a média
const calcularMedia = (numeros) => {
  if (numeros.length === 0) return 0;

  let soma = numeros.reduce((total, num) => total + num, 0);
  return soma / numeros.length;
};

// Array de exemplo
const numeros = [3, 8, 12, 5, 7, 20, 11, 6];

// 1. Filtrar os pares
const pares = filtrarPares(numeros);

// 2. Calcular a média dos pares
const mediaPares = calcularMedia(pares);

// 3. Exibir no console
console.log("Números originais:", numeros);
console.log("Números pares:", pares);
console.log("Média dos pares:", mediaPares);