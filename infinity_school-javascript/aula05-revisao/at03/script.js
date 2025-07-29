let idade = parseInt(prompt("Qual a sua idade?"));

if (idade <= 12 || idade >= 60) {
  console.log("Você tem direito ao desconto na entrada do cinema.");
} else {
  console.log("Você não tem direito ao desconto.");
}

// Verificando se a bilheteria está aberta (aberta das 13h às 22h)
let horaAtual = new Date().getHours();

if (horaAtual >= 13 && horaAtual <= 22) {
  console.log("A bilheteria está aberta.");
} else {
  console.log("A bilheteria está fechada.");
}

// Verificando status de exibição do filme
let horaTerminoFilme = 21; // exemplo: filme termina às 21h

if (horaAtual < horaTerminoFilme) {
  console.log("O filme ainda está em exibição.");
} else {
  console.log("A exibição do filme já terminou.");
}