// Pega os elementos do HTML
const link = document.getElementById("meuLink");
const mensagem = document.getElementById("mensagem");

// Evento de clique no link
link.addEventListener("click", (event) => {
  event.preventDefault(); // Impede o redirecionamento

  mensagem.textContent = "Você clicou no link, mas não foi redirecionado."; // Mostra mensagem
});