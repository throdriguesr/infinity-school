// função chamada quando o usuário clica no botão
function solicitarIdade() {
  // pega o valor digitado
  let valor = document.getElementById("idade").value;
  // elemento onde aparece a mensagem
  let resultado = document.getElementById("resultado");

  try {
    // transforma o valor em número inteiro
    let idade = parseInt(valor, 10);

    // se não for número, lança erro
    if (isNaN(idade)) {
      throw new Error("Idade inválida: não é um número.");
    }

    // se for menor que zero, lança erro
    if (idade < 0) {
      throw new Error("Idade inválida: não pode ser menor que zero.");
    }

    // mostra idade válida
    resultado.textContent = "Idade válida: " + idade;
  } catch (erro) {
    // mostra a mensagem de erro
    resultado.textContent = "Erro: " + erro.message;
  } finally {
    // mensagem no console sempre aparece
    console.log("Verificação concluída.");
  }
}