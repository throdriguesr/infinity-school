// Atividade 03
// Crie um código que peça ao usuário para adivinhar um número entre 1 e 10, repetindo o pedido até que o usuário acerte. 
// Defina o número a ser adivinhado diretamente no código.

// Objetivo:
// Aprender a utilizar a estrutura de repetição while (true) para criar um jogo simples de adivinhação.

let numeroSecreto = 7;
let palpite;

while (true) {
  palpite = parseInt(prompt("Adivinhe o número entre 1 e 10:"));

  if (palpite === numeroSecreto) {
    alert("Você acertou!");
    break;
  }
}