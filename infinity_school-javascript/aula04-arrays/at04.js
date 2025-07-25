// Atividade 04
// Crie um script que contenha um array de números e utilize o loop for
// para percorrê-lo. Para cada número no array, verifique se ele é par ou
// ímpar e exiba uma mensagem no console indicando o resultado.
//
// Objetivo:
// Praticar o uso do loop for para percorrer arrays e aplicar lógica
// condicional para verificar se os números são pares ou ímpares.

let numeros = [5, 12, 7, 8, 3, 10];

for (let i = 0; i < numeros.length; i++) {
  if (numeros[i] % 2 === 0) {
    console.log(numeros[i] + " é par");
  } else {
    console.log(numeros[i] + " é ímpar");
  }
}