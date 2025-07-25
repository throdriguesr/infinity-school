// Atividade 05
// Crie um código JavaScript que itere de 1 a 20 usando um loop for.
// Use continue para pular iterações quando o número for múltiplo de 3 e break para sair do loop quando o número for maior que 15. 
// Exiba os números processados no console com console.log.
//
// Objetivo:
// Aprender a utilizar as instruções break e continue para controlar o fluxo dos loops ao filtrar números.

for (let i = 1; i <= 20; i++) {
  if (i > 15) {
    break;
  }

  if (i % 3 === 0) {
    continue;
  }

  console.log(i);
}