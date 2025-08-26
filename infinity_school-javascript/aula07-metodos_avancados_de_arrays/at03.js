/*
Atividade 03
Crie um script que utilize o método filter() para filtrar um array de
números, mantendo apenas os números pares. O script deve
armazenar os números pares em um novo array e exibi-lo no
console.

Objetivo:
Praticar o uso do método filter() para criar um novo array contendo
apenas os elementos que atendem a uma condição específica.
*/

const numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

const numerosPares = numeros.filter(function(numero) {
    return numero % 2 === 0;
});

console.log(numerosPares);