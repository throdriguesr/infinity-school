// Solicita dois números do usuário (como texto)
let numero1 = prompt("Digite o primeiro número:");
let numero2 = prompt("Digite o segundo número:");

// Converte os textos para números
numero1 = Number(numero1);
numero2 = Number(numero2);

// Cópia do primeiro número para usar com operadores de atribuição
let resultado = numero1;

// Adição
resultado += numero2; // mesmo que resultado = resultado + numero2
console.log("Resultado da adição (+=):", resultado);

// Subtração
resultado = numero1; // reinicia o valor
resultado -= numero2;
console.log("Resultado da subtração (-=):", resultado);

// Multiplicação
resultado = numero1;
resultado *= numero2;
console.log("Resultado da multiplicação (*=):", resultado);

// Divisão
resultado = numero1;
resultado /= numero2;
console.log("Resultado da divisão (/=):", resultado);

// Resto da divisão
resultado = numero1;
resultado %= numero2;
console.log("Resultado do resto (%=):", resultado);