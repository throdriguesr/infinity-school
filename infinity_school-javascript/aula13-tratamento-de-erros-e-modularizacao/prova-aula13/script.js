// captura o formulário
const form = document.getElementById("cadastroForm");

// escuta o envio do formulário
form.addEventListener("submit", function(event) {
  // impede recarregar a página
  event.preventDefault();

  // limpa mensagens de erro anteriores
  limparErros();

  try {
    // lê valores digitados
    const nome = document.getElementById("nome").value.trim();
    const usuario = document.getElementById("usuario").value.trim();
    const senha = document.getElementById("senha").value.trim();
    const email = document.getElementById("email").value.trim();
    const idade = parseInt(document.getElementById("idade").value);

    // validações simples
    if (nome.length < 3) {
      throw { campo: "nome", mensagem: "O nome precisa ter pelo menos 3 letras." };
    }

    if (usuario.length < 3) {
      throw { campo: "usuario", mensagem: "O usuário precisa ter pelo menos 3 letras." };
    }

    if (senha.length < 6) {
      throw { campo: "senha", mensagem: "A senha precisa ter pelo menos 6 caracteres." };
    }

    if (!email.includes("@") || !email.includes(".")) {
      throw { campo: "email", mensagem: "Email inválido." };
    }

    if (isNaN(idade) || idade < 18) {
      throw { campo: "idade", mensagem: "A idade deve ser um número válido e maior ou igual a 18." };
    }

    // se tudo passou, mostra sucesso
    document.getElementById("mensagemFinal").textContent = "Cadastro realizado com sucesso!";
    document.getElementById("mensagemFinal").style.color = "green";

  } catch (erro) {
    // mostra mensagem de erro no campo certo
    const erroCampo = document.getElementById("erro-" + erro.campo);
    if (erroCampo) {
      erroCampo.textContent = erro.mensagem;
    }
    // mensagem final limpa
    document.getElementById("mensagemFinal").textContent = "";
  }
});

// função para limpar mensagens antigas
function limparErros() {
  document.querySelectorAll(".erro").forEach(e => e.textContent = "");
  document.getElementById("mensagemFinal").textContent = "";
}