// Pega os elementos do HTML
const formulario = document.getElementById("meuFormulario");
const limparBtn = document.getElementById("limparLista");
const lista = document.getElementById("listaDados");

// Função que adiciona os dados na lista
formulario.addEventListener("submit", (event) => {
  event.preventDefault(); // Impede envio do formulário

  // Pega os valores
  const usuario = document.getElementById("usuario").value.trim();
  const senha = document.getElementById("senha").value.trim();
  const telefone = document.getElementById("telefone").value.trim();
  const nascimento = document.getElementById("nascimento").value;
  const email = document.getElementById("email").value.trim();

  // Validação simples
  if (!usuario || !senha || !telefone || !nascimento || !email) {
    console.error("Todos os campos devem ser preenchidos!");
    return; // Não adiciona se algum campo estiver vazio
  }

  // Cria item da lista com os dados
  const li = document.createElement("li");
  li.textContent = `Usuário: ${usuario}, Senha: ${senha}, Telefone: ${telefone}, Nascimento: ${nascimento}, E-mail: ${email}`;

  // Adiciona à lista
  lista.appendChild(li);

  // Limpa o formulário
  formulario.reset();
});

// Limpa a lista ao clicar no botão
limparBtn.addEventListener("click", () => {
  lista.innerHTML = ""; // Remove todos os elementos
});