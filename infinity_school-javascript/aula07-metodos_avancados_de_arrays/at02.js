/*
Atividade 02
Crie um script que utilize o método map() para transformar um array de
números. A transformação deve consistir em calcular o quadrado de
cada número do array original. O script deve então armazenar os
resultados em um novo array e exibi-lo no console.

Objetivo:
Praticar o uso do método map() para criar um novo array a partir de uma
transformação aplicada aos elementos de um array existente.
*/

const numeros = [2, 4, -3, 5, 0];

const quadrados = numeros.map(function(numero) {
    return numero * numero;
});

console.log(quadrados);