// função chamada ao clicar no botão
function dividir() {
  // lê os valores dos inputs
  const v1 = document.getElementById("num1").value;
  const v2 = document.getElementById("num2").value;
  // elemento de resultado
  const resultado = document.getElementById("resultado");

  try {
    // converte para número
    const a = parseFloat(v1);
    const b = parseFloat(v2);

    // valida se são números
    if (isNaN(a) || isNaN(b)) {
      throw new Error("Ambos os valores devem ser números.");
    }

    // lança erro se divisor for zero
    if (b === 0) {
      throw new Error("Divisão por zero não é permitida.");
    }

    // mostra o resultado quando tudo ok
    resultado.textContent = "Resultado: " + (a / b);
  } catch (erro) {
    // mostra a mensagem de erro na tela
    resultado.textContent = "Erro: " + erro.message;
    // exibe o nome e a mensagem do erro no console
    console.error(erro.name + ": " + erro.message);
  } finally {
    // executa sempre
    console.log("Operação finalizada.");
  }
}