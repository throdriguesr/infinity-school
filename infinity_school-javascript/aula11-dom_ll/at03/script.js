// Pega os elementos do HTML
const tituloInput = document.getElementById("tituloInput");
const descricaoInput = document.getElementById("descricaoInput");
const botao = document.getElementById("adicionarCartao");
const container = document.getElementById("container");

// Adiciona um cartão ao clicar no botão
botao.addEventListener("click", () => {
  const titulo = tituloInput.value.trim();
  const descricao = descricaoInput.value.trim();

  if (titulo === "" || descricao === "") return; // Não adiciona se estiver vazio

  // Cria a div do cartão
  const cartao = document.createElement("div");
  cartao.classList.add("cartao");

  // Cria título e parágrafo
  const h3 = document.createElement("h3");
  h3.textContent = titulo;

  const p = document.createElement("p");
  p.textContent = descricao;

  // Adiciona título e parágrafo ao cartão
  cartao.appendChild(h3);
  cartao.appendChild(p);

  // Adiciona o cartão ao container
  container.appendChild(cartao);

  // Limpa os campos
  tituloInput.value = "";
  descricaoInput.value = "";
});