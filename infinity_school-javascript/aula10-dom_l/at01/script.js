// Seleciona todos os parágrafos
const paragrafos = document.getElementsByTagName("p");

// Loop para alterar o texto de cada parágrafo
for (let i = 0; i < paragrafos.length; i++) {
  paragrafos[i].textContent = "Texto alterado";
}