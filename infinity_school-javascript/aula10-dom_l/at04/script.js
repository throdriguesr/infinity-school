// Pega os elementos do HTML
const adicionarBtn = document.getElementById("adicionarParagrafo");
const removerBtn = document.getElementById("removerParagrafo");
const container = document.getElementById("container");

// Contador para numerar os parágrafos
let contador = 1;

// Função para adicionar parágrafo
adicionarBtn.addEventListener("click", () => {
  const p = document.createElement("p"); // Cria um novo parágrafo
  p.textContent = "Parágrafo " + contador; // Define o texto
  container.appendChild(p); // Adiciona no container
  contador++; // Incrementa o contador
});

// Função para remover o último parágrafo
removerBtn.addEventListener("click", () => {
  const paragrafo = container.lastElementChild; // Pega o último parágrafo
  if (paragrafo) {
    container.removeChild(paragrafo); // Remove do container
    contador--; // Decrementa o contador
  }
});