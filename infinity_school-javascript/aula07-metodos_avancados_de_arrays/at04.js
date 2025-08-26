/*
Atividade 04
Crie um script que utilize o método reduce() para somar todos os números de um array. O script deve calcular a soma total e exibir o resultado no console.

Objetivo:
Praticar o uso do método reduce() para acumular valores em um array, resultando em um único valor.
*/

const numeros = [1, 2, 3, 4, 5];

const somaTotal = numeros.reduce(function(acumulador, numero) {
    return acumulador + numero;
}, 0);

console.log("A soma total é:", somaTotal);