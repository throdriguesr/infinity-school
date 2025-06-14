// Solicita o primeiro número e converte para número
let numero1 = Number(prompt("Digite o primeiro número:"));

// Solicita o segundo número e converte para número
let numero2 = Number(prompt("Digite o segundo número:"));

// Verifica se ambos são positivos
let ambosPositivos = (numero1 > 0) && (numero2 > 0);

// Verifica se pelo menos um é positivo
let peloMenosUmPositivo = (numero1 > 0) || (numero2 > 0);

// Verifica se nenhum é positivo (negação de peloMenosUmPositivo)
let nenhumPositivo = !peloMenosUmPositivo;

// Exibe os resultados no console
console.log("Ambos são positivos? " + ambosPositivos);
console.log("Pelo menos um é positivo? " + peloMenosUmPositivo);
console.log("Nenhum é positivo? " + nenhumPositivo);