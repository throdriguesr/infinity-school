// Pega os elementos
const inputNome = document.getElementById("nomeUsuario");
const btnSalvar = document.getElementById("salvarBtn");
const exibirNome = document.getElementById("exibirNome");

// Carrega o nome salvo no localStorage ao iniciar a página
window.addEventListener("load", () => {
  const nomeSalvo = localStorage.getItem("nomeUsuario");
  if (nomeSalvo) {
    exibirNome.textContent = `Nome armazenado: ${nomeSalvo}`;
  }
});

// Salva o nome ao clicar no botão
btnSalvar.addEventListener("click", () => {
  const nome = inputNome.value.trim();
  if (nome) {
    localStorage.setItem("nomeUsuario", nome); // Salva no localStorage
    exibirNome.textContent = `Nome armazenado: ${nome}`;
    inputNome.value = ""; // Limpa o campo
  }
});