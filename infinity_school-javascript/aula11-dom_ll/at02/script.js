// Pega os elementos do HTML
const input = document.getElementById("itemInput");
const botao = document.getElementById("adicionarItem");
const lista = document.getElementById("lista");

// Adiciona item à lista ao clicar no botão
botao.addEventListener("click", () => {
  const texto = input.value.trim(); // Pega o texto do input
  if (texto === "") return; // Não adiciona se estiver vazio

  const li = document.createElement("li"); // Cria um novo item da lista
  li.textContent = texto; // Define o texto do item
  lista.appendChild(li); // Adiciona à lista

  input.value = ""; // Limpa o input
});