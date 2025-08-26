/*
Atividade 05
Crie um script que utilize o método some() para verificar se um array contém algum número negativo. 
O script deve exibir no console uma mensagem indicando se há ou não números negativos no array.

Objetivo:
Praticar o uso do método some() para verificar se pelo menos um elemento em um array atende a uma condição específica.
*/

const numeros = [3, 7, -2, 5, 0];

const temNegativo = numeros.some(function(numero) {
    return numero < 0;
});

if (temNegativo) {
    console.log("O array contém pelo menos um número negativo.");
} else {
    console.log("O array não contém números negativos.");
}