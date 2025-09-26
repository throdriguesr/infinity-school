// função que valida os dados do usuário
function validarUsuario() {
  // pega os valores digitados
  let nome = document.getElementById("nome").value;
  let idade = parseInt(document.getElementById("idade").value);
  let resultado = document.getElementById("resultado");

  // cria o objeto do usuário
  let usuario = { nome: nome, idade: idade };

  try {
    // valida se o nome tem pelo menos 3 letras
    if (usuario.nome.length < 3) {
      throw new Error("O nome precisa ter pelo menos 3 letras.");
    }

    // valida se a idade é positiva e maior que 18
    if (isNaN(usuario.idade) || usuario.idade <= 0) {
      throw new Error("A idade precisa ser um número positivo.");
    }
    if (usuario.idade <= 18) {
      throw new Error("A idade precisa ser maior que 18.");
    }

    // se passou em tudo, mostra sucesso
    resultado.textContent = "Usuário válido!";
  } catch (erro) {
    // se der erro, mostra a mensagem
    resultado.textContent = "Erro: " + erro.message;
  } finally {
    // aparece sempre, mesmo se der erro ou não
    console.log("Validação finalizada.");
  }
}