const nomes = [];

while (true) {
  let entrada = prompt("Digite um nome (ou 'sair' para finalizar):");
  if (entrada === null) {
    break;
  }
  entrada = entrada.trim();
  if (entrada.toLowerCase() === "sair") {
    break;
  }
  if (entrada !== "") {
    nomes.push(entrada);
  }
}

// Exibir nomes com índices usando for
for (let i = 0; i < nomes.length; i++) {
  console.log(`${i + 1}: ${nomes[i]}`);
}

// Exibir mensagem personalizada usando for...of
for (const nome of nomes) {
  console.log(`Bem-vindo(a), ${nome}!`);
}