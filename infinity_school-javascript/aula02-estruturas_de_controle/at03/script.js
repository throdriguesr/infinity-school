// Solicita ao usuário um número
let numero = Number(prompt("Digite um número:"));

// Verifica se o número é positivo, negativo ou zero
if (numero > 0) {
    console.log("O número é positivo.");
} else if (numero < 0) {
    console.log("O número é negativo.");
} else {
    console.log("O número é zero.");
}