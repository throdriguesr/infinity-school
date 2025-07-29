function gerarTriangulo() {
  const n = parseInt(document.getElementById("numero").value);

  if (isNaN(n) || n <= 0) {
    console.log("Por favor, insira um número inteiro positivo.");
    return;
  }

  for (let i = n; i >= 1; i--) {
    let linha = "";
    for (let j = 1; j <= i; j++) {
      linha += j + " ";
    }
    console.log(linha.trim());
  }
}