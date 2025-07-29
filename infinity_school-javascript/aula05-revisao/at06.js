// [Atividade 06]
// Crie um arquivo JavaScript e siga os passos abaixo para praticar o uso de loops.
//
// 1. Usando um loop for, exiba no console todos os números de 1 a 10.
//
// 2. Usando um loop while, exiba no console todos os números pares de 2 a 20.
//
// 3. Usando um loop for, crie uma variável chamada soma que acumule a soma dos números de 1 a 5
//    e exiba o resultado no final.
//
// Objetivo:
// Compreender e praticar o uso de loops for e while.

console.log("Números de 1 a 10:");
for (let i = 1; i <= 10; i++) {
  console.log(i);
}

console.log("Números pares de 2 a 20:");
let num = 2;
while (num <= 20) {
  console.log(num);
  num += 2;
}

let soma = 0;
for (let i = 1; i <= 5; i++) {
  soma += i;
}
console.log("Soma dos números de 1 a 5:", soma);