// Atividade 02
// Escreva um código que utilize a estrutura do...while para solicitar ao usuário que insira um número. 
// O loop deve continuar pedindo ao usuário até que um número negativo seja inserido.

// Objetivo:
// Aprender a utilizar a estrutura de repetição do...while para executar um bloco de código pelo menos uma vez e, em seguida, repetir a execução enquanto a condição especificada for verdadeira.

let numero;

do {
  numero = parseFloat(prompt("Digite um número:"));
} while (numero >= 0);