const form = document.getElementById("formTarefa");
const input = document.getElementById("tituloTarefa");
const lista = document.getElementById("listaTarefas");

let tarefas = JSON.parse(localStorage.getItem("tarefas")) || [];

// renderiza todas as tarefas
function renderizarTarefas() {
  lista.innerHTML = "";

  tarefas.forEach((tarefa, index) => {
    const li = document.createElement("li");
    li.className = tarefa.concluida ? "concluida" : "";

    li.innerHTML = `
      <span>${tarefa.titulo}</span>
      <div>
        <button class="editar">Editar</button>
        <button class="excluir">Excluir</button>
      </div>
    `;

    // marcar/desmarcar tarefa
    li.querySelector("span").addEventListener("click", () => {
      tarefa.concluida = !tarefa.concluida;
      salvarTarefas();
      renderizarTarefas();
    });

    // editar tarefa
    li.querySelector(".editar").addEventListener("click", () => {
      const novoTitulo = prompt("Editar tarefa:", tarefa.titulo);
      if (novoTitulo !== null && novoTitulo.trim() !== "") {
        tarefa.titulo = novoTitulo.trim();
        salvarTarefas();
        renderizarTarefas();
      }
    });

    // remover tarefa
    li.querySelector(".excluir").addEventListener("click", () => {
      tarefas.splice(index, 1);
      salvarTarefas();
      renderizarTarefas();
    });

    lista.appendChild(li);
  });
}

// salva tarefas no Local Storage
function salvarTarefas() {
  localStorage.setItem("tarefas", JSON.stringify(tarefas));
}

// adicionar nova tarefa
form.addEventListener("submit", (e) => {
  e.preventDefault();

  const titulo = input.value.trim();
  if (titulo === "") return;

  tarefas.push({ titulo, concluida: false });
  salvarTarefas();
  renderizarTarefas();
  input.value = "";
});

// inicializa
renderizarTarefas();