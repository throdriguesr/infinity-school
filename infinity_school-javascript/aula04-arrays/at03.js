// Atividade 03
// Crie um array chamado cores contendo as seguintes cores, Vermelho, Verde, Azul.
//
// Adicione as cores Amarelo e Roxo ao final do array.
// Em seguida, remova a última cor.
// Use o método splice para remover "Verde" e adicionar "Laranja" e "Marrom" em seu lugar.
// Crie um novo array chamado novasCores contendo as primeiras duas cores do array cores.
// Use o método join para criar uma string com todas as cores do array cores, separadas por uma vírgula.
// Inverta a ordem dos elementos no array cores.
// Exiba os arrays cores e novasCores, e a string resultante no console.
//
// Objetivo:
// Praticar operações básicas de criação, acesso e modificação de elementos em arrays.

let cores = ["Vermelho", "Verde", "Azul"];

cores.push("Amarelo");
cores.push("Roxo");
cores.pop();

let indiceVerde = cores.indexOf("Verde");
if (indiceVerde !== -1) {
  cores.splice(indiceVerde, 1, "Laranja", "Marrom");
}

let novasCores = cores.slice(0, 2);

let coresString = cores.join(",");

cores.reverse();

console.log(cores);
console.log(novasCores);
console.log(coresString);