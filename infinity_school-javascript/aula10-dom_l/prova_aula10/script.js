// Pega os elementos do HTML
const tarefaInput = document.getElementById("tarefaInput");
const adicionarBtn = document.getElementById("adicionarBtn");
const listaTarefas = document.getElementById("listaTarefas");

// Função para adicionar uma tarefa
function adicionarTarefa() {
  const texto = tarefaInput.value.trim(); // Pega o texto do input
  if (texto === "") return; // Não adiciona se estiver vazio

  // Cria um novo item da lista
  const li = document.createElement("li");
  li.textContent = texto;

  // Adiciona clique para marcar como concluída
  li.addEventListener("click", () => {
    li.classList.toggle("concluida");
  });

  // Cria botão de remover
  const removerBtn = document.createElement("button");
  removerBtn.textContent = "Remover";

  // Adiciona clique para remover a tarefa
  removerBtn.addEventListener("click", (e) => {
    e.stopPropagation(); // Evita marcar como concluída ao remover
    listaTarefas.removeChild(li);
  });

  // Adiciona o botão ao item da lista
  li.appendChild(removerBtn);

  // Adiciona o item à lista
  listaTarefas.appendChild(li);

  // Limpa o input
  tarefaInput.value = "";
}

// Evento para o botão "Adicionar Tarefa"
adicionarBtn.addEventListener("click", adicionarTarefa);

// Permite adicionar a tarefa apertando Enter
tarefaInput.addEventListener("keypress", (e) => {
  if (e.key === "Enter") {
    adicionarTarefa();
  }
});