// Atividade 04
// Escreva um programa que faça o seguinte:
// Peça ao usuário para inserir um número inteiro positivo.
// Utilize um loop while para calcular e exibir a soma de todos os números inteiros de 1 até o número inserido pelo usuário.
// Exiba o resultado em um alerta ou no console.
//
// Objetivo:
// Praticar o uso da estrutura while para iterar um número específico de vezes, manipulando entradas do usuário e realizando operações aritméticas simples.

let numero = parseInt(prompt("Digite um número inteiro positivo:"));
let contador = 1;
let soma = 0;

while (contador <= numero) {
  soma += contador;
  contador++;
}

console.log("A soma dos números de 1 até " + numero + " é: " + soma);