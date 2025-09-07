// Pega os elementos do HTML
const imagem = document.getElementById("minhaImagem");
const link = document.getElementById("meuLink");
const botao = document.getElementById("meuBotao");

// Quando clicar no botão, muda os atributos
botao.addEventListener("click", () => {
  // Altera a imagem
  imagem.setAttribute("src", "https://atletico.com.br/wp-content/uploads/2022/04/ESCUDOS-GALO-927x1024.jpg");

  // Altera o link
  link.setAttribute("href", "https://atletico.com.br/");
  link.textContent = "Acesse o site do GALO";
});