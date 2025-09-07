// Seleciona todas as divs com a classe "box"
const divs = document.querySelectorAll(".box");

// Array de cores para cada div
const cores = ["lightblue", "lightgreen", "lightcoral"];

// Loop para alterar a cor de fundo de cada div
divs.forEach((div, index) => {
  div.style.backgroundColor = cores[index];
});