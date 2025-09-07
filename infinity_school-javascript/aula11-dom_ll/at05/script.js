// Pega os elementos do HTML
const formulario = document.getElementById("meuFormulario");
const input = document.getElementById("textoInput");
const resultado = document.getElementById("resultado");

// Evento para capturar o envio do formulário
formulario.addEventListener("submit", (event) => {
  event.preventDefault(); // Impede envio do formulário

  const valor = input.value.trim(); // Pega o valor do input
  if (valor === "") return; // Não faz nada se estiver vazio

  resultado.textContent = "Você digitou: " + valor; // Mostra na página

  input.value = ""; // Limpa o input
});