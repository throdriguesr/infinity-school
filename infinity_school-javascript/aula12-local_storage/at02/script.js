// Pega os elementos
const inputTarefa = document.getElementById("tarefaInput");
const btnSalvar = document.getElementById("salvarBtn");
const btnRemover = document.getElementById("removerBtn");
const btnLimpar = document.getElementById("limparBtn");
const exibirTarefa = document.getElementById("exibirTarefa");

// Carrega a tarefa salva (se existir)
window.addEventListener("load", () => {
  const tarefaSalva = localStorage.getItem("tarefa");
  if (tarefaSalva) {
    exibirTarefa.textContent = `Tarefa armazenada: ${tarefaSalva}`;
  }
});

// Salvar tarefa
btnSalvar.addEventListener("click", () => {
  const tarefa = inputTarefa.value.trim();
  if (tarefa) {
    localStorage.setItem("tarefa", tarefa);
    exibirTarefa.textContent = `Tarefa armazenada: ${tarefa}`;
    inputTarefa.value = ""; // limpa o campo
  }
});

// Remover tarefa específica
btnRemover.addEventListener("click", () => {
  localStorage.removeItem("tarefa");
  exibirTarefa.textContent = "Nenhuma tarefa armazenada.";
});

// Limpar todas as tarefas
btnLimpar.addEventListener("click", () => {
  localStorage.clear();
  exibirTarefa.textContent = "Todas as tarefas foram removidas.";
});