let lista = [];

while (true) {
  let opcao = prompt(
    "Escolha uma opção:\n1 - Adicionar item\n2 - Remover item\n3 - Atualizar item\n4 - Exibir lista\n5 - Sair"
  );

  if (opcao === "1") {
    let item = prompt("Digite o nome do item para adicionar:");
    if (item) {
      lista.push(item);
    }
  } else if (opcao === "2") {
    let indice = prompt("Digite o índice do item que deseja remover:");
    indice = parseInt(indice);
    if (!isNaN(indice) && indice >= 0 && indice < lista.length) {
      lista.splice(indice, 1);
    } else {
      alert("Índice inválido.");
    }
  } else if (opcao === "3") {
    let indice = prompt("Digite o índice do item que deseja atualizar:");
    indice = parseInt(indice);
    if (!isNaN(indice) && indice >= 0 && indice < lista.length) {
      let novoItem = prompt("Digite o novo valor para o item:");
      lista[indice] = novoItem;
    } else {
      alert("Índice inválido.");
    }
  } else if (opcao === "4") {
    console.clear();
    if (lista.length === 0) {
      console.log("A lista está vazia.");
    } else {
      for (let i = 0; i < lista.length; i++) {
        console.log(i + ": " + lista[i]);
      }
    }
  } else if (opcao === "5") {
    break;
  } else {
    alert("Opção inválida.");
  }
}