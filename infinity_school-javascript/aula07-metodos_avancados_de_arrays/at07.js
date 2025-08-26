/*
Atividade 07
Crie um script que utilize o método every() para verificar se todos os números em um array são positivos. 
O script deve exibir no console uma mensagem indicando se todos os números são positivos ou se há algum número negativo ou zero no array.

Objetivo:
Praticar o uso do método every() para verificar se todos os elementos em um array atendem a uma condição específica.
*/

const numeros = [3, 5, 7, 2, 9];

const todosPositivos = numeros.every(function(numero) {
    return numero > 0;
});

if (todosPositivos) {
    console.log("Todos os números do array são positivos.");
} else {
    console.log("Há pelo menos um número negativo ou zero no array.");
}