// Pega os elementos da página
const temaSelect = document.getElementById("temaSelect");
const fonteSelect = document.getElementById("fonteSelect");
const salvarBtn = document.getElementById("salvarBtn");
const status = document.getElementById("status");
const body = document.body;

// Função para aplicar as escolhas na tela
function aplicarPreferencias(preferencias) {
  // Remove estilos antigos
  body.classList.remove("tema-claro", "tema-escuro", "fonte-pequena", "fonte-media", "fonte-grande");

  // Aplica o tema
  if (preferencias.tema === "escuro") {
    body.classList.add("tema-escuro");
  } else {
    body.classList.add("tema-claro");
  }

  // Aplica o tamanho da fonte
  if (preferencias.fonte === "pequeno") {
    body.classList.add("fonte-pequena");
  } else if (preferencias.fonte === "grande") {
    body.classList.add("fonte-grande");
  } else {
    body.classList.add("fonte-media");
  }

  // Atualiza a mensagem
  status.textContent = `Tema: ${preferencias.tema}, Fonte: ${preferencias.fonte}`;
}

// Quando a página carrega
window.addEventListener("load", () => {
  // Busca no localStorage o que já está salvo
  const salvo = localStorage.getItem("preferencias");

  if (salvo) {
    // Transforma a string em objeto com JSON.parse()
    const preferencias = JSON.parse(salvo);

    // Ajusta os selects
    temaSelect.value = preferencias.tema;
    fonteSelect.value = preferencias.fonte;

    // Aplica na página
    aplicarPreferencias(preferencias);
  }
});

// Quando o botão salvar é clicado
salvarBtn.addEventListener("click", () => {
  // Pega os valores escolhidos
  const preferencias = {
    tema: temaSelect.value,
    fonte: fonteSelect.value
  };

  // Salva no localStorage como string com JSON.stringify()
  localStorage.setItem("preferencias", JSON.stringify(preferencias));

  // Aplica na página
  aplicarPreferencias(preferencias);

  // Mostra mensagem confirmando
  status.textContent = `Preferências salvas — Tema: ${preferencias.tema}, Fonte: ${preferencias.fonte}`;
});