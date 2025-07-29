let idade = parseInt(prompt("Digite sua idade:"));

if (idade < 18) {
  console.log("Você é menor de idade.");
} else if (idade <= 65) {
  console.log("Você é um adulto.");
} else {
  console.log("Você é idoso.");
}