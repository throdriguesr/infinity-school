// Array para armazenar tarefas
let tarefas = [];

// Função para adicionar tarefa
function adicionarTarefa() {
  const input = document.getElementById("novaTarefa");
  const tarefaTexto = input.value.trim();

  if (tarefaTexto === "") {
    alert("Por favor, digite uma tarefa.");
    return;
  }

  tarefas.push({ texto: tarefaTexto, concluida: false });
  input.value = "";
  mostrarTarefas();
}

// Função para mostrar a lista de tarefas atualizada
function mostrarTarefas() {
  const lista = document.getElementById("tarefas");
  lista.innerHTML = "";

  tarefas.forEach((tarefa, index) => {
    const li = document.createElement("li");
    li.textContent = tarefa.concluida ? "✅ " + tarefa.texto : tarefa.texto;
    if (tarefa.concluida) {
      li.classList.add("concluida");
    }

    // Botão concluir
    const btnConcluir = document.createElement("button");
    btnConcluir.textContent = "Concluir";
    btnConcluir.onclick = () => {
      tarefas[index].concluida = true;
      mostrarTarefas();
    };

    // Botão remover
    const btnRemover = document.createElement("button");
    btnRemover.textContent = "Remover";
    btnRemover.onclick = () => {
      tarefas.splice(index, 1);
      mostrarTarefas();
    };

    li.appendChild(btnConcluir);
    li.appendChild(btnRemover);
    lista.appendChild(li);
  });
}