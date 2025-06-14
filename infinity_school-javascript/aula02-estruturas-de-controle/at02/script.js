// Solicita o primeiro número e converte para número
let numero1 = Number(prompt("Digite o primeiro número:"));

// Solicita o segundo número e converte para número
let numero2 = Number(prompt("Digite o segundo número:"));

// Comparações usando operadores de comparação

console.log(numero1 + " == " + numero2 + " ?", numero1 == numero2);   // igualdade só valor
console.log(numero1 + " === " + numero2 + " ?", numero1 === numero2); // igualdade valor e tipo
console.log(numero1 + " != " + numero2 + " ?", numero1 != numero2);   // diferente só valor
console.log(numero1 + " !== " + numero2 + " ?", numero1 !== numero2); // diferente valor ou tipo
console.log(numero1 + " < " + numero2 + " ?", numero1 < numero2);     // menor que
console.log(numero1 + " > " + numero2 + " ?", numero1 > numero2);     // maior que
console.log(numero1 + " <= " + numero2 + " ?", numero1 <= numero2);   // menor ou igual
console.log(numero1 + " >= " + numero2 + " ?", numero1 >= numero2);   // maior ou igual