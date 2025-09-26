function dividir() {
  // pega o valor que a pessoa digitou e transforma em número
  let num1 = parseFloat(document.getElementById("num1").value);
  let num2 = parseFloat(document.getElementById("num2").value);
  let resultado = document.getElementById("resultado");

  try {
    // tenta fazer a divisão
    if (num2 === 0) {
      // se o número de baixo for zero, joga erro
      throw new Error("Não dá pra dividir por zero!");
    }

    // mostra o resultado se estiver tudo certo
    resultado.textContent = "Resultado: " + (num1 / num2);
  } catch (erro) {
    // se der erro, mostra a mensagem
    resultado.textContent = "Erro: " + erro.message;
  } finally {
    // aparece sempre, mesmo se der erro ou não
    console.log("Operação concluída!");
  }
}