// Pega os elementos do HTML
const notaInput = document.getElementById("notaInput");
const adicionarNotaBtn = document.getElementById("adicionarNotaBtn");
const listaNotas = document.getElementById("listaNotas");

// Chave para salvar as notas no localStorage
const STORAGE_KEY = "notas";

// Array de notas em memória
let notas = [];

// Carregar notas ao abrir a página
window.addEventListener("load", () => {
  const salvo = localStorage.getItem(STORAGE_KEY);
  if (salvo) {
    notas = JSON.parse(salvo);
  } else {
    notas = [];
  }
  renderizarNotas();
});

// Salvar as notas no localStorage
function salvarNotas() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(notas));
}

// Renderizar a lista de notas
function renderizarNotas() {
  listaNotas.innerHTML = "";

  notas.forEach((nota) => {
    const li = document.createElement("li");
    li.classList.add("nota-item");

    // Texto da nota
    const span = document.createElement("span");
    span.textContent = nota.titulo;

    // Botão remover
    const btnRemover = document.createElement("button");
    btnRemover.textContent = "Remover";
    btnRemover.classList.add("btn-remover");
    btnRemover.addEventListener("click", () => removerNota(nota.id));

    li.appendChild(span);
    li.appendChild(btnRemover);
    listaNotas.appendChild(li);
  });

  if (notas.length === 0) {
    const vazio = document.createElement("p");
    vazio.textContent = "Nenhuma nota cadastrada.";
    listaNotas.appendChild(vazio);
  }
}

// Adicionar uma nova nota
adicionarNotaBtn.addEventListener("click", () => {
  const titulo = notaInput.value.trim();
  if (titulo === "") return;

  // Verifica se já existe uma nota com o mesmo título
  const existe = notas.some(n => n.titulo.toLowerCase() === titulo.toLowerCase());
  if (existe) {
    alert("Já existe uma nota com esse título!");
    return;
  }

  const novaNota = {
    id: Date.now().toString(),
    titulo: titulo
  };

  notas.push(novaNota);
  salvarNotas();
  renderizarNotas();
  notaInput.value = "";
});

// Remover nota pelo ID
function removerNota(id) {
  notas = notas.filter(n => n.id !== id);
  salvarNotas();
  renderizarNotas();
}

// Permitir adicionar com Enter
notaInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter") {
    adicionarNotaBtn.click();
  }
});