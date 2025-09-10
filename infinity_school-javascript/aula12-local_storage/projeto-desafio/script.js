// Pega os elementos do HTML
const tarefaInput = document.getElementById("tarefaInput");
const adicionarBtn = document.getElementById("adicionarBtn");
const limparBtn = document.getElementById("limparBtn");
const listaTarefas = document.getElementById("listaTarefas");

// Chave usada no localStorage
const STORAGE_KEY = "tarefas";

// Array que guarda as tarefas em memória
let tarefas = [];

// Id da tarefa que está sendo editada (null se não estiver editando)
let editandoId = null;

// Carrega as tarefas do localStorage ao abrir a página
window.addEventListener("load", () => {
  const salvo = localStorage.getItem(STORAGE_KEY);
  if (salvo) {
    // Converte a string salva para array com JSON.parse()
    tarefas = JSON.parse(salvo);
  } else {
    tarefas = [];
  }
  renderizarLista();
});

// Salva o array de tarefas no localStorage (usa JSON.stringify())
function salvarTarefas() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(tarefas));
}

// Renderiza a lista de tarefas na tela
function renderizarLista() {
  listaTarefas.innerHTML = ""; // Limpa a lista

  // Para cada tarefa, cria um item com texto, editar e excluir
  tarefas.forEach((tarefa) => {
    const li = document.createElement("li");
    li.classList.add("tarefa-item");

    // Texto da tarefa
    const span = document.createElement("span");
    span.classList.add("tarefa-texto");
    span.textContent = tarefa.texto;

    // Botão editar
    const btnEditar = document.createElement("button");
    btnEditar.textContent = "Editar";
    btnEditar.classList.add("btn-pequeno", "editar");
    btnEditar.addEventListener("click", () => iniciarEdicao(tarefa.id));

    // Botão excluir
    const btnExcluir = document.createElement("button");
    btnExcluir.textContent = "Excluir";
    btnExcluir.classList.add("btn-pequeno", "excluir");
    btnExcluir.addEventListener("click", () => excluirTarefa(tarefa.id));

    // Monta o item
    li.appendChild(span);
    li.appendChild(btnEditar);
    li.appendChild(btnExcluir);

    listaTarefas.appendChild(li);
  });

  // Se não houver tarefas, mostra mensagem simples
  if (tarefas.length === 0) {
    const vazio = document.createElement("p");
    vazio.textContent = "Nenhuma tarefa cadastrada.";
    listaTarefas.appendChild(vazio);
  }
}

// Adiciona nova tarefa ou atualiza a que está em edição
adicionarBtn.addEventListener("click", () => {
  const texto = tarefaInput.value.trim();
  if (texto === "") return; // não faz nada se vazio

  if (editandoId) {
    // Atualiza tarefa existente
    const index = tarefas.findIndex(t => t.id === editandoId);
    if (index > -1) {
      tarefas[index].texto = texto;
      salvarTarefas();
      renderizarLista();
      // Limpa estado de edição
      editandoId = null;
      adicionarBtn.textContent = "Adicionar Tarefa";
      tarefaInput.value = "";
    }
  } else {
    // Cria nova tarefa com id único
    const novaTarefa = {
      id: Date.now().toString(),
      texto: texto
    };
    tarefas.push(novaTarefa);
    salvarTarefas();
    renderizarLista();
    tarefaInput.value = "";
  }
});

// Inicia edição: carrega texto no input e muda o botão
function iniciarEdicao(id) {
  const tarefa = tarefas.find(t => t.id === id);
  if (!tarefa) return;
  tarefaInput.value = tarefa.texto;
  editandoId = id;
  adicionarBtn.textContent = "Atualizar Tarefa";
  tarefaInput.focus();
}

// Exclui a tarefa do array e do localStorage
function excluirTarefa(id) {
  tarefas = tarefas.filter(t => t.id !== id);
  salvarTarefas();
  renderizarLista();
}

// Limpa todas as tarefas (innerHTML = "" no localStorage + array)
limparBtn.addEventListener("click", () => {
  tarefas = [];
  salvarTarefas();
  renderizarLista();
});

// Permite pressionar Enter para adicionar/atualizar
tarefaInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter") {
    adicionarBtn.click();
  }
});