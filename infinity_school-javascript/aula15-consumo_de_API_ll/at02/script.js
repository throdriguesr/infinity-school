// dados simulados de cada página
const apiSimulada = {
  1: ["Item 1-1", "Item 1-2", "Item 1-3"],
  2: ["Item 2-1", "Item 2-2", "Item 2-3"],
  3: ["Item 3-1", "Item 3-2", "Item 3-3"]
};

// página inicial
let paginaAtual = 1;

// função para buscar dados de uma página
function buscarPagina(pagina) {
  console.log("Carregando dados da página", pagina, "...");

  // delay artificial para simular tempo de resposta
  setTimeout(() => {
    const dados = apiSimulada[pagina];
    console.log("Dados da página", pagina, ":", dados);
  }, 1000); // 1 segundo de delay
}

// funções para navegar
function proximaPagina() {
  if (paginaAtual < 3) {
    paginaAtual++;
    buscarPagina(paginaAtual);
  } else {
    console.log("Última página atingida");
  }
}

function paginaAnterior() {
  if (paginaAtual > 1) {
    paginaAtual--;
    buscarPagina(paginaAtual);
  } else {
    console.log("Primeira página atingida");
  }
}

// inicia exibindo a página 1
buscarPagina(paginaAtual);