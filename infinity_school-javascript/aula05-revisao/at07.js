// [Atividade 07]
// Crie um programa que faça o seguinte:
//
// Geração de Dados:
// - Crie um array chamado numeros contendo 20 números inteiros aleatórios entre 1 e 100.
//
// Manipulação de Dados:
// - Filtre os números pares do array e armazene-os em um novo array chamado pares.
// - Transforme o array pares para que cada número seja elevado ao quadrado.
// - Calcule a soma de todos os números no array transformado.
//
// Exibição:
// - Exiba no console o array original, o array de números pares,
//   o array de números ao quadrado e a soma final.
//
// Objetivo:
// Praticar a manipulação de arrays utilizando métodos avançados,
// como filter, map e reduce, para realizar operações complexas de
// transformação e agregação de dados.

// Criar um array com 20 números aleatórios entre 1 e 100
let numeros = [];

for (let i = 0; i < 20; i++) {
  let numeroAleatorio = Math.floor(Math.random() * 100) + 1;
  numeros.push(numeroAleatorio);
}

// Filtrar os números pares
let pares = numeros.filter(function(numero) {
  return numero % 2 === 0;
});

// Elevar cada número par ao quadrado
let quadrados = pares.map(function(numero) {
  return numero * numero;
});

// Somar todos os números ao quadrado
let soma = quadrados.reduce(function(total, numero) {
  return total + numero;
}, 0);

// Exibir os resultados no console
console.log("Array original:", numeros);
console.log("Números pares:", pares);
console.log("Pares ao quadrado:", quadrados);
console.log("Soma dos quadrados dos pares:", soma);