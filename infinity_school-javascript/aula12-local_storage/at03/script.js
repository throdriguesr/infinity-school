// Pega os elementos do HTML
const temaSelect = document.getElementById("temaSelect");
const fonteSelect = document.getElementById("fonteSelect");
const salvarBtn = document.getElementById("salvarBtn");
const status = document.getElementById("status");
const body = document.body;

// Aplica as preferências na página
function aplicarPreferencias(pref) {
  // Remove classes antigas
  body.classList.remove("tema-claro", "tema-escuro", "fonte-pequena", "fonte-media", "fonte-grande");

  // Adiciona a classe do tema
  if (pref.tema === "escuro") {
    body.classList.add("tema-escuro");
  } else {
    body.classList.add("tema-claro");
  }

  // Adiciona a classe do tamanho da fonte
  if (pref.fonte === "pequeno") {
    body.classList.add("fonte-pequena");
  } else if (pref.fonte === "grande") {
    body.classList.add("fonte-grande");
  } else {
    body.classList.add("fonte-media");
  }

  // Atualiza texto de status
  status.textContent = `Tema: ${pref.tema}, Fonte: ${pref.fonte}`;
}

// Carrega preferências ao abrir a página
window.addEventListener("load", () => {
  const salvo = localStorage.getItem("preferencias");
  let preferencias;

  if (salvo) {
    // Recupera preferências armazenadas
    try {
      preferencias = JSON.parse(salvo);
    } catch {
      preferencias = { tema: "claro", fonte: "medio" };
    }
  } else {
    // Padrões se não existir nada salvo
    preferencias = { tema: "claro", fonte: "medio" };
  }

  // Ajusta os selects para refletir as preferências
  temaSelect.value = preferencias.tema;
  fonteSelect.value = preferencias.fonte;

  // Aplica as preferências na página
  aplicarPreferencias(preferencias);
});

// Salva preferências ao clicar em "Salvar"
salvarBtn.addEventListener("click", () => {
  const preferencias = {
    tema: temaSelect.value,
    fonte: fonteSelect.value
  };

  // Salva no localStorage como string
  localStorage.setItem("preferencias", JSON.stringify(preferencias));

  // Aplica imediatamente
  aplicarPreferencias(preferencias);

  // Mensagem curta de confirmação
  status.textContent = `Preferências salvas — Tema: ${preferencias.tema}, Fonte: ${preferencias.fonte}`;
});