/*
Atividade 06
Crie um script que utilize o método find() para localizar o primeiro número ímpar em um array de números. 
O script deve exibir no console o número encontrado ou uma mensagem indicando que não há números ímpares no array.

Objetivo:
Praticar o uso do método find() para buscar e retornar o primeiro elemento em um array que satisfaz uma condição específica.
*/

const numeros = [2, 4, 6, 7, 8];

const primeiroImpar = numeros.find(function(numero) {
    return numero % 2 !== 0;
});

if (primeiroImpar !== undefined) {
    console.log("O primeiro número ímpar é:", primeiroImpar);
} else {
    console.log("Não há números ímpares no array.");
}