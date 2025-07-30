// Lista de tarefas (cada tarefa é um objeto com descrição e status)
let tarefas = [];

// Função anônima para adicionar tarefa
const adicionarTarefa = function(tarefa) {
  tarefas.push({ descricao: tarefa, concluida: false });
  console.log("Tarefa adicionada:", tarefa);
};

// Arrow function para listar tarefas
const listarTarefas = () => {
  if (tarefas.length === 0) {
    console.log("Nenhuma tarefa cadastrada.");
    return;
  }

  console.log("Lista de tarefas:");
  tarefas.forEach((tarefa, index) => {
    const status = tarefa.concluida ? "Concluída" : "Pendente";
    console.log(index + ": " + tarefa.descricao + " - " + status);
  });
};

// Função de ordem superior com callback
function processarTarefa(indice, callback) {
  if (indice >= 0 && indice < tarefas.length) {
    callback(indice);
  } else {
    console.log("Índice inválido.");
  }
}

// Callbacks
const removerTarefa = (indice) => {
  console.log("Tarefa removida:", tarefas[indice].descricao);
  tarefas.splice(indice, 1);
};

const atualizarTarefa = (indice) => {
  let novaDescricao = prompt("Digite a nova descrição da tarefa:");
  if (novaDescricao) {
    tarefas[indice].descricao = novaDescricao;
    console.log("Tarefa atualizada.");
  } else {
    console.log("Descrição inválida.");
  }
};

const concluirTarefa = (indice) => {
  tarefas[indice].concluida = true;
  console.log("Tarefa marcada como concluída.");
};

// Menu de interação
let opcao;

do {
  opcao = prompt(
    "Escolha uma opção:\n" +
    "1 - Adicionar tarefa\n" +
    "2 - Listar tarefas\n" +
    "3 - Remover tarefa\n" +
    "4 - Atualizar tarefa\n" +
    "5 - Concluir tarefa\n" +
    "0 - Sair"
  );

  switch (opcao) {
    case "1":
      let novaTarefa = prompt("Digite a tarefa:");
      if (novaTarefa) {
        adicionarTarefa(novaTarefa);
      } else {
        console.log("Tarefa inválida.");
      }
      break;

    case "2":
      listarTarefas();
      break;

    case "3":
      listarTarefas();
      let indiceRemover = parseInt(prompt("Digite o índice da tarefa a remover:"));
      processarTarefa(indiceRemover, removerTarefa);
      break;

    case "4":
      listarTarefas();
      let indiceAtualizar = parseInt(prompt("Digite o índice da tarefa a atualizar:"));
      processarTarefa(indiceAtualizar, atualizarTarefa);
      break;

    case "5":
      listarTarefas();
      let indiceConcluir = parseInt(prompt("Digite o índice da tarefa a concluir:"));
      processarTarefa(indiceConcluir, concluirTarefa);
      break;

    case "0":
      console.log("Programa encerrado.");
      break;

    default:
      console.log("Opção inválida.");
  }

} while (opcao !== "0");