/*
Atividade 01
Crie um script que contenha um array com alguns números e utilize o
método forEach() para percorrê-lo. Para cada número no array, verifique
se ele é positivo, negativo ou zero, e exiba uma mensagem no console
indicando o resultado.

Objetivo:
Praticar o uso do método forEach() para iterar sobre os elementos de um
array, aplicando lógica condicional para verificar e classificar os números
como positivos, negativos ou zero.
*/

const numeros = [10, -5, 0, 7, -3];

numeros.forEach(function(numero) {
    if (numero > 0) {
        console.log(numero + " é positivo");
    } else if (numero < 0) {
        console.log(numero + " é negativo");
    } else {
        console.log(numero + " é zero");
    }
});